"""
=========================================================
Module: farm_plan_service.py

Purpose:
    Coordinates farm planning business logic and
    database persistence.

Responsibilities:
    - Generate farm plans
    - Save farm plans
    - Retrieve farm plans
    - Update farm plans
    - Delete farm plans
    - Pagination
    - Search
    - Filtering
    - Statistics

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date, timedelta

from app.database.models import FarmPlanModel
from app.planner.schedule_generator import generate_schedule
from app.repositories.farm_plan_repository import FarmPlanRepository

from app.schemas.farm_plan_create import FarmPlanCreate
from app.schemas.farm_plan_update import FarmPlanUpdate


class FarmPlanService:
    """
    Service layer responsible for coordinating business
    logic between the API and the database.
    """

    def __init__(self, repository: FarmPlanRepository):
        """
        Initialize the service with a repository instance.
        """
        self.repository = repository

    # =====================================================
    # SERIALIZATION
    # =====================================================

    def _serialize_for_database(self, data):
        """
        Recursively convert Python objects into
        JSON-serializable values.
        """

        if isinstance(data, dict):
            return {
                key: self._serialize_for_database(value)
                for key, value in data.items()
            }

        if isinstance(data, list):
            return [
                self._serialize_for_database(item)
                for item in data
            ]

        if isinstance(data, date):
            return data.isoformat()

        if isinstance(data, timedelta):
            return data.days

        return data

    # =====================================================
    # GENERATE FARM PLAN
    # =====================================================

    def generate_plan(
        self,
        request: FarmPlanCreate
    ):
        """
        Generate a farm plan, save it to the database,
        and return the saved farm plan.
        """

        result = generate_schedule(request)

        db_result = self._serialize_for_database(result)

        model = FarmPlanModel(
            crop=db_result["crop"],
            planting_date=date.fromisoformat(
                db_result["planting_date"]
            ),
            activities=db_result["activities"],
            resource_report=db_result["resource_report"],
            conflicts=db_result["conflicts"],
            recommendations=db_result["recommendations"],
            calendar=db_result["calendar"]
        )

        return self.repository.create(model)

    # =====================================================
    # CREATE
    # =====================================================

    def save_plan(
        self,
        plan: FarmPlanModel
    ):
        """
        Save a farm plan directly to the database.
        """
        return self.repository.create(plan)

    # =====================================================
    # READ ALL
    # =====================================================

    def get_all_plans(self):
        """
        Retrieve all farm plans.
        """
        return self.repository.get_all()

    # =====================================================
    # PAGINATED READ
    # =====================================================

    def get_paginated_plans(
        self,
        page: int,
        size: int
    ):
        """
        Retrieve paginated farm plans.
        """

        skip = (page - 1) * size

        plans = self.repository.get_paginated(
            skip=skip,
            limit=size
        )

        total = self.repository.count()

        return {
            "page": page,
            "size": size,
            "total": total,
            "data": plans
        }

    # =====================================================
    # READ ONE
    # =====================================================

    def get_plan_by_id(
        self,
        plan_id: int
    ):
        """
        Retrieve a farm plan by its ID.
        """
        return self.repository.get_by_id(plan_id)

    # =====================================================
    # SEARCH
    # =====================================================

    def search_plans_by_crop(
        self,
        crop: str
    ):
        """
        Search farm plans by crop.
        """
        return self.repository.search_by_crop(crop)

    # =====================================================
    # FILTER
    # =====================================================

    def filter_plans_by_planting_date(
        self,
        planting_date: date
    ):
        """
        Filter farm plans by planting date.
        """
        return self.repository.filter_by_planting_date(
            planting_date
        )

    # =====================================================
    # UPDATE
    # =====================================================

    def update_plan(
        self,
        plan_id: int,
        request: FarmPlanUpdate
    ):
        """
        Update an existing farm plan.
        """

        updated_data = self._serialize_for_database(
            request.model_dump()
        )

        updated_data["planting_date"] = date.fromisoformat(
            updated_data["planting_date"]
        )

        return self.repository.update(
            plan_id,
            updated_data
        )

    # =====================================================
    # DELETE
    # =====================================================

    def delete_plan(
        self,
        plan: FarmPlanModel
    ):
        """
        Delete a farm plan.
        """
        return self.repository.delete(plan)

    # =====================================================
    # STATISTICS
    # =====================================================

    def get_statistics(self):
        """
        Retrieve farm plan statistics.
        """
        return self.repository.get_statistics()