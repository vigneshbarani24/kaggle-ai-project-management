import json
import os
from typing import List, Dict, Any
from models import CompanyProfile, FinancialAnalysis, ERPTriggers, Stakeholder, LeadScore, FullReport
from tools import Tools

class BaseAgent:
    def __init__(self, name: str, tools: Tools):
        self.name = name
        self.tools = tools

    def call_llm(self, prompt: str, output_schema: Any = None) -> str:
        """
        Simulates an LLM call. In production, use google.generativeai or OpenAI.
        """
        print(f"[{self.name}] Thinking...")
        
        # Extract company name from prompt for dynamic mock data
        company_name = "Target Company"
        if "for " in prompt:
            try:
                # Naive extraction: "Analyze ... for CompanyName: ..."
                parts = prompt.split("for ")
                if len(parts) > 1:
                    company_name = parts[1].split(":")[0].strip()
            except:
                pass

        if output_schema == CompanyProfile:
            return json.dumps({
                "name": company_name,
                "domain": f"{company_name.lower().replace(' ', '')}.com",
                "industry": "Private Equity / Investment",
                "description": f"{company_name} is a leading firm in its sector.",
                "competitors": ["Competitor A", "Competitor B"]
            })
        elif output_schema == FinancialAnalysis:
            return json.dumps({
                "revenue": "$500 Million+",
                "growth_rate": "10%",
                "it_budget_estimate": "$20 Million",
                "financial_health": "Strong"
            })
        elif output_schema == ERPTriggers:
            return json.dumps({
                "current_erp": "Legacy System / Excel",
                "pain_points": ["Consolidation issues", "Manual reporting", "Lack of scalability"],
                "trigger_events": ["Portfolio expansion", "Digital transformation mandate"],
                "cloud_readiness": "Medium"
            })
        elif output_schema == List[Stakeholder]: 
             return json.dumps([
                {
                    "name": "Alex Finance",
                    "title": "CFO",
                    "linkedin_url": f"https://linkedin.com/in/alex-{company_name.lower()}",
                    "relevance": "Controls the budget."
                },
                {
                    "name": "Sam Tech",
                    "title": "CTO",
                    "linkedin_url": f"https://linkedin.com/in/sam-{company_name.lower()}",
                    "relevance": "Leads technology strategy."
                }
            ])
        elif output_schema == LeadScore:
            return json.dumps({
                "score": 75,
                "reasoning": f"{company_name} shows signs of needing better consolidation tools due to growth.",
                "citations": [f"https://www.{company_name.lower().replace(' ', '')}.com"]
            })
        
        return "Generic LLM response"

class ResearchAgent(BaseAgent):
    def run(self, company_name: str) -> CompanyProfile:
        search_results = self.tools.search_web(f"{company_name} company profile industry competitors")
        prompt = f"Analyze these search results for {company_name}: {search_results}"
        response_json = self.call_llm(prompt, output_schema=CompanyProfile)
        return CompanyProfile(**json.loads(response_json))

class FinancialAgent(BaseAgent):
    def run(self, company_profile: CompanyProfile) -> FinancialAnalysis:
        search_results = self.tools.search_web(f"{company_profile.name} revenue financial report annual report")
        prompt = f"Analyze financials for {company_profile.name}: {search_results}"
        response_json = self.call_llm(prompt, output_schema=FinancialAnalysis)
        return FinancialAnalysis(**json.loads(response_json))

class SignalAgent(BaseAgent):
    def run(self, company_profile: CompanyProfile) -> ERPTriggers:
        search_results = self.tools.search_web(f"{company_profile.name} technology stack ERP SAP Oracle job openings")
        prompt = f"Identify ERP signals for {company_profile.name}: {search_results}"
        response_json = self.call_llm(prompt, output_schema=ERPTriggers)
        return ERPTriggers(**json.loads(response_json))

class StakeholderAgent(BaseAgent):
    def run(self, company_profile: CompanyProfile) -> List[Stakeholder]:
        search_results = self.tools.search_web(f"{company_profile.name} CIO CTO VP Supply Chain CFO")
        prompt = f"Find stakeholders for {company_profile.name}: {search_results}"
        response_json = self.call_llm(prompt, output_schema=List[Stakeholder])
        data = json.loads(response_json)
        return [Stakeholder(**item) for item in data]

class ScoringAgent(BaseAgent):
    def run(self, profile: CompanyProfile, financials: FinancialAnalysis, triggers: ERPTriggers, stakeholders: List[Stakeholder]) -> LeadScore:
        prompt = f"Score this lead based on: {profile}, {financials}, {triggers}, {stakeholders}"
        response_json = self.call_llm(prompt, output_schema=LeadScore)
        return LeadScore(**json.loads(response_json))

class CopywriterAgent(BaseAgent):
    def run(self, profile: CompanyProfile, triggers: ERPTriggers, stakeholders: List[Stakeholder]) -> str:
        prompt = f"Write a cold email to {stakeholders[0].name} at {profile.name} about {triggers.pain_points}"
        return f"Subject: Transforming {profile.name}'s Operations\n\nHi {stakeholders[0].name},\n\nI noticed {profile.name}'s recent expansion..."
