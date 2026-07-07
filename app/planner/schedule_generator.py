from fastapi import HTTPException

from app.schemas.farm_plan import FarmPlanRequest
from app.planner.crop_rules import CROP_RULES


def generate_schedule(request: FarmPlanRequest):

    rules = CROP_RULES.get(request.crop)

    if rules is None:
        raise HTTPException(
            status_code=400,
            detail=f"Crop '{request.crop}' is not supported."
        )

    activities = []

    for activity in rules["activities"]:

        activity_date = request.planting_date + activity["offset"]

        activities.append(
            {
                "activity": activity["name"],
                "date": activity_date
            }
        )

    return {
        "crop": request.crop,
        "planting_date": request.planting_date,
        "activities": activities
    }