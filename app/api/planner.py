from fastapi import APIRouter

from app.schemas.farm_plan import FarmPlanRequest
from app.planner.schedule_generator import generate_schedule
from app.schemas.farm_plan_response import FarmPlanResponse

router = APIRouter()


@router.post(
    "/generate-plan",
    response_model=FarmPlanResponse
)
def generate_plan(request: FarmPlanRequest):

    schedule = generate_schedule(request)

    return schedule