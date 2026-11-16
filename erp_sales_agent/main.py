import argparse
import json
from tools import Tools
from agents import ResearchAgent, FinancialAgent, SignalAgent, StakeholderAgent, ScoringAgent, CopywriterAgent
from models import FullReport

def main():
    parser = argparse.ArgumentParser(description="ERP Sales BDR Agent")
    parser.add_argument("--company", type=str, required=True, help="Target company name")
    args = parser.parse_args()

    print(f"🚀 Starting ERP Sales Mission for: {args.company}")
    
    tools = Tools()
    
    # Initialize Agents
    researcher = ResearchAgent("ResearchAgent", tools)
    finance_analyst = FinancialAgent("FinancialAgent", tools)
    signal_hunter = SignalAgent("SignalAgent", tools)
    headhunter = StakeholderAgent("StakeholderAgent", tools)
    scorer = ScoringAgent("ScoringAgent", tools)
    copywriter = CopywriterAgent("CopywriterAgent", tools)

    # 1. Research
    print("\n--- Step 1: Company Research ---")
    profile = researcher.run(args.company)
    print(f"Found: {profile.name} ({profile.domain})")

    # 2. Financials
    print("\n--- Step 2: Financial Analysis ---")
    financials = finance_analyst.run(profile)
    print(f"Revenue: {financials.revenue}, Health: {financials.financial_health}")

    # 3. Signals
    print("\n--- Step 3: ERP Signal Detection ---")
    triggers = signal_hunter.run(profile)
    print(f"Current ERP: {triggers.current_erp}")
    print(f"Triggers: {', '.join(triggers.trigger_events)}")

    # 4. Stakeholders
    print("\n--- Step 4: Finding Stakeholders ---")
    stakeholders = headhunter.run(profile)
    for s in stakeholders:
        print(f"- {s.name} ({s.title})")

    # 5. Scoring
    print("\n--- Step 5: Lead Scoring ---")
    score = scorer.run(profile, financials, triggers, stakeholders)
    print(f"Lead Score: {score.score}/100")
    print(f"Reasoning: {score.reasoning}")

    # 6. Pitch
    print("\n--- Step 6: Drafting Pitch ---")
    pitch = copywriter.run(profile, triggers, stakeholders)
    print(f"\n{pitch}")

    # Final Report
    report = FullReport(
        company_profile=profile,
        financial_analysis=financials,
        erp_triggers=triggers,
        stakeholders=stakeholders,
        lead_score=score,
        generated_pitch=pitch
    )
    
    # Save to file
    filename = f"{args.company.replace(' ', '_')}_report.json"
    with open(filename, "w") as f:
        f.write(report.model_dump_json(indent=2))
    print(f"\n✅ Report saved to {filename}")

if __name__ == "__main__":
    main()
