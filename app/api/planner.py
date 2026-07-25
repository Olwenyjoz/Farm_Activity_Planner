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

from datetime import date
from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.repositories.farm_plan_repository import FarmPlanRepository
from app.services.farm_plan_service import FarmPlanService

from app.schemas.farm_plan_create import FarmPlanCreate
from app.schemas.farm_plan_update import FarmPlanUpdate
from app.schemas.farm_plan_response import FarmPlanResponse

router = APIRouter()


# =====================================================
# GENERATE FARM PLAN
# =====================================================

@router.post(
    "/generate-plan",
    response_model=FarmPlanResponse,
    status_code=status.HTTP_201_CREATED
)
def generate_plan(
    request: FarmPlanCreate,
    db: Session = Depends(get_db)
):
    """
    Generate a farm plan,
    save it to the database,
    and return the saved farm plan.
    """

    repository = FarmPlanRepository(db)
    service = FarmPlanService(repository)

    return service.generate_plan(request)


# =====================================================
# GET ALL FARM PLANS
# =====================================================

@router.get(
    "/farm-plans",
    response_model=List[FarmPlanResponse],
    status_code=status.HTTP_200_OK
)
def get_all_farm_plans(
    db: Session = Depends(get_db)
):
    """
    Retrieve all farm plans.
    """

    repository = FarmPlanRepository(db)
    service = FarmPlanService(repository)

    return service.get_all_plans()


# =====================================================
# PAGINATED FARM PLANS
# =====================================================

@router.get(
    "/farm-plans/paginated",
    status_code=status.HTTP_200_OK
)
def get_paginated_farm_plans(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Retrieve farm plans using pagination.
    """

    repository = FarmPlanRepository(db)
    service = FarmPlanService(repository)

    return service.get_paginated_plans(
        page=page,
        size=size
    )


# =====================================================
# SEARCH FARM PLANS
# =====================================================

@router.get(
    "/farm-plans/search",
    response_model=List[FarmPlanResponse],
    status_code=status.HTTP_200_OK
)
def search_farm_plans(
    crop: str,
    db: Session = Depends(get_db)
):
    """
    Search farm plans by crop.
    """

    repository = FarmPlanRepository(db)
    service = FarmPlanService(repository)

    return service.search_plans_by_crop(crop)


# =====================================================
# FILTER FARM PLANS
# =====================================================

@router.get(
    "/farm-plans/filter",
    response_model=List[FarmPlanResponse],
    status_code=status.HTTP_200_OK
)
def filter_farm_plans(
    planting_date: date,
    db: Session = Depends(get_db)
):
    """
    Filter farm plans by planting date.
    """

    repository = FarmPlanRepository(db)
    service = FarmPlanService(repository)

    return service.filter_plans_by_planting_date(
        planting_date
    )


# =====================================================
# FARM PLAN STATISTICS
# =====================================================

@router.get(
    "/farm-plans/statistics",
    status_code=status.HTTP_200_OK
)
def get_statistics(
    db: Session = Depends(get_db)
):
    """
    Retrieve farm plan statistics.
    """

    repository = FarmPlanRepository(db)
    service = FarmPlanService(repository)

    return service.get_statistics()


# =====================================================
# GET FARM PLAN BY ID
# =====================================================

@router.get(
    "/farm-plans/{plan_id}",
    response_model=FarmPlanResponse,
    status_code=status.HTTP_200_OK
)
def get_farm_plan_by_id(
    plan_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a farm plan by its ID.
    """

    repository = FarmPlanRepository(db)
    service = FarmPlanService(repository)

    plan = service.get_plan_by_id(plan_id)

    if plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm plan not found."
        )

    return plan


# =====================================================
# UPDATE FARM PLAN
# =====================================================

@router.put(
    "/farm-plans/{plan_id}",
    response_model=FarmPlanResponse,
    status_code=status.HTTP_200_OK
)
def update_farm_plan(
    plan_id: int,
    request: FarmPlanUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing farm plan.
    """

    repository = FarmPlanRepository(db)
    service = FarmPlanService(repository)

    updated_plan = service.update_plan(
        plan_id,
        request
    )

    if updated_plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm plan not found."
        )

    return updated_plan


# =====================================================
# DELETE FARM PLAN
# =====================================================

@router.delete(
    "/farm-plans/{plan_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_farm_plan(
    plan_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete a farm plan by its ID.
    """

    repository = FarmPlanRepository(db)
    service = FarmPlanService(repository)

    plan = service.get_plan_by_id(plan_id)

    if plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Farm plan not found."
        )

    service.delete_plan(plan)

    return