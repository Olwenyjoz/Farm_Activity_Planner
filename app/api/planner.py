from fastapi import APIRouter

from app.schemas.farm_plan import FarmPlanRequest

router = APIRouter()


@router.post("/generate-plan")
def generate_plan(request: FarmPlanRequest):
    return {
  "message": "Farm plan received successfully",
  "data": {
    "crop": "Maize",
    "planting_date": "2026-07-15",
    "farm_size": 5.0,
    "workers": 8
  }
}