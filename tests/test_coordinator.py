from datetime import date

from app.agents.coordinator import Coordinator
from app.schemas.farm_plan_create import FarmPlanCreate

agent = Coordinator()

request = FarmPlanCreate(

    crop="Maize",

    planting_date=date(2026,8,10),

    farm_size=5,

    workers=4,

    latitude=-1.286389,

    longitude=36.817223,

    soil_type="Loamy",

    season="Rainy"
)

plan = agent.execute(request)

print(plan)