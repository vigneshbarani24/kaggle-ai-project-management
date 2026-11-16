from pydantic import BaseModel, Field
from typing import List, Optional

class CompanyProfile(BaseModel):
    name: str = Field(description="Name of the company")
    domain: str = Field(description="Domain name of the company")
    industry: str = Field(description="Primary industry of the company")
    description: str = Field(description="Brief description of the company")
    competitors: List[str] = Field(description="List of top competitors")

class FinancialAnalysis(BaseModel):
    revenue: str = Field(description="Annual revenue estimate")
    growth_rate: str = Field(description="Year-over-year growth rate")
    it_budget_estimate: str = Field(description="Estimated IT budget or spending")
    financial_health: str = Field(description="Assessment of financial health (e.g., Strong, Stable, Weak)")

class ERPTriggers(BaseModel):
    current_erp: str = Field(description="Inferred current ERP system (e.g., SAP ECC, Oracle EBS, Legacy)")
    pain_points: List[str] = Field(description="List of potential pain points with current system")
    trigger_events: List[str] = Field(description="Recent events triggering need for change (e.g., M&A, Expansion, Compliance)")
    cloud_readiness: str = Field(description="Assessment of readiness for cloud migration")

class Stakeholder(BaseModel):
    name: str = Field(description="Name of the stakeholder")
    title: str = Field(description="Job title")
    linkedin_url: Optional[str] = Field(description="LinkedIn profile URL")
    relevance: str = Field(description="Why this person is a key decision maker for ERP")

class LeadScore(BaseModel):
    score: int = Field(description="Lead score from 0 to 100")
    reasoning: str = Field(description="Detailed reasoning for the score")
    citations: List[str] = Field(description="List of sources/URLs used for the analysis")

class FullReport(BaseModel):
    company_profile: CompanyProfile
    financial_analysis: FinancialAnalysis
    erp_triggers: ERPTriggers
    stakeholders: List[Stakeholder]
    lead_score: LeadScore
    generated_pitch: str = Field(description="Drafted cold email pitch")
