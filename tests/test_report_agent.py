from datetime import date

from app.agents.planner_agent import PlannerAgent
from app.agents.report_agent import ReportAgent
from app.schemas.farm_plan_create import FarmPlanCreate

planner = PlannerAgent()
report_agent = ReportAgent()

request = FarmPlanCreate(
    crop="Maize",
    planting_date=date(2026, 8, 10),
    farm_size=5,
    workers=4,
    latitude=-1.286389,
    longitude=36.817223,
    soil_type="Loamy",
    season="Rainy"
)

plan = planner.generate_plan(request)

report = report_agent.generate_report(plan)

print(report)