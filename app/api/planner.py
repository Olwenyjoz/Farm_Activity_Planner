"""
=========================================================
Module: planner.py

Purpose:
    Farm Planning API Endpoints

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.repositories.farm_plan_repository import (
    FarmPlanRepository
)

from app.services.farm_plan_service import (
    FarmPlanService
)

from app.schemas.farm_plan import FarmPlanRequest
from app.schemas.farm_plan_response import (
    FarmPlanResponse
)

router = APIRouter()


# =====================================================
# GENERATE FARM PLAN
# =====================================================

@router.post(
    "/generate-plan",
    response_model=FarmPlanResponse
)
def generate_plan(

    request: FarmPlanRequest,

    db: Session = Depends(get_db)

):
    """
    Generate a farm plan, save it to the database,
    and return the generated response.
    """

    repository = FarmPlanRepository(db)

    service = FarmPlanService(repository)

    return service.generate_plan(request)