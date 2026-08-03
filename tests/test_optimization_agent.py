from datetime import date

from app.agents.optimization_agent import OptimizationAgent
from app.agents.planner_agent import PlannerAgent
from app.schemas.farm_plan_create import FarmPlanCreate

planner = PlannerAgent()

optimizer = OptimizationAgent()

request = FarmPlanCreate(
    crop="Maize",
    planting_date=date(2026, 8, 10),
    farm_size=12,
    workers=15,
    latitude=-1.286389,
    longitude=36.817223,
    soil_type="Loamy",
    season="Rainy"
)

plan = planner.generate_plan(request)

optimized = optimizer.optimize(plan)

print(optimized["recommendations"])