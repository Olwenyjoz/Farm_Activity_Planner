from fastapi import APIRouter

from app.schemas.farm_plan import FarmPlanRequest
from app.planner.schedule_generator import generate_schedule

router = APIRouter()


@router.post("/generate-plan")
def generate_plan(request: FarmPlanRequest):

    schedule = generate_schedule(request)

    return schedule