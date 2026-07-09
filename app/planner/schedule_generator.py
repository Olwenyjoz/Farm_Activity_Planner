from fastapi import HTTPException

from app.schemas.farm_plan import FarmPlanRequest

from app.planner.crop_rules import CROP_RULES
from app.planner.resource_allocator import generate_resource_report
from app.planner.conflict_detector import detect_worker_conflicts


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
            **activity,
            "date": activity_date
            }
        )

    schedule = {
    "crop": request.crop,
    "planting_date": request.planting_date,
    "activities": activities
    }
    
    resource_report = generate_resource_report(schedule)
    
    conflicts = detect_worker_conflicts(
    schedule,
    request.workers
    )
    
    return {
    **schedule,
    "resource_report": resource_report,
    "conflicts": conflicts
    }