from app.schemas.farm_plan import FarmPlanRequest
from app.planner.crop_rules import CROP_RULES


def generate_schedule(request: FarmPlanRequest):

    rules = CROP_RULES.get(request.crop)

    if rules is None:
        raise ValueError(f"Crop '{request.crop}' is not supported.")

    first_weeding = request.planting_date + rules["first_weeding"]

    harvest = request.planting_date + rules["harvest"]

    return {
        "crop": request.crop,
        "planting_date": request.planting_date,
        "activities": [
            {
                "activity": "First Weeding",
                "date": first_weeding
            },
            {
                "activity": "Harvest",
                "date": harvest
            }
        ]
    }