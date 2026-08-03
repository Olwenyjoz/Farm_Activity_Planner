"""
=========================================================
Module: farm_plan_service.py

Purpose:
    Coordinates farm planning business logic and
    database persistence.

Responsibilities:
    - Generate farm plans
    - Weather integration
    - CRUD operations
    - Pagination
    - Search
    - Filtering
    - Statistics
    - User ownership

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date
from datetime import timedelta

from app.database.models import FarmPlanModel
from app.repositories.farm_plan_repository import FarmPlanRepository

from app.schemas.farm_plan_create import FarmPlanCreate
from app.schemas.farm_plan_update import FarmPlanUpdate

from app.agents.coordinator import Coordinator


class FarmPlanService:
    """
    Service layer responsible for business logic.
    """

    def __init__(
        self,
        repository: FarmPlanRepository
    ):
        """
        Initialize the Farm Plan Service.

        Responsibilities:
            - Manage database persistence.
            - Coordinate CRUD operations.
            - Delegate intelligent planning
            to the Coordinator Agent.
        """

        self.repository = repository

        self.coordinator = Coordinator()
            
    # =====================================================
    # SERIALIZATION
    # =====================================================

    def _serialize(self, value):
        """
        Convert dates and timedeltas into JSON serializable values.
        """

        if isinstance(value, dict):
            return {
                k: self._serialize(v)
                for k, v in value.items()
            }

        if isinstance(value, list):
            return [
                self._serialize(item)
                for item in value
            ]

        if isinstance(value, date):
            return value.isoformat()

        if isinstance(value, timedelta):
            return value.days

        return value

    # =====================================================
    # GENERATE FARM PLAN
    # =====================================================

    def generate_plan(
        self,
        request: FarmPlanCreate,
        current_user
    ):
        """
        Generate a complete farm activity plan for the
        authenticated user using the Multi-Agent
        Coordinator.

        Workflow:
            1. Execute the Coordinator Agent.
            2. Convert planner output into JSON-serializable data.
            3. Create the database model.
            4. Persist the plan.
            5. Return the saved farm plan.
        """

        # -------------------------------------------------
        # Step 1: Execute the Multi-Agent workflow.
        # -------------------------------------------------

        planner_result = self.coordinator.execute(
            request
        )

        # -------------------------------------------------
        # Step 2: Convert planner output into
        # JSON-serializable objects.
        # -------------------------------------------------

        planner_result = self._serialize(
            planner_result
        )

        # -------------------------------------------------
        # Step 3: Create the FarmPlan database object.
        # -------------------------------------------------

        model = FarmPlanModel(

            user_id=current_user.id,

            crop=planner_result["crop"],

            planting_date=date.fromisoformat(
                planner_result["planting_date"]
            ),

            farm_size=request.farm_size,

            workers=request.workers,

            latitude=request.latitude,

            longitude=request.longitude,

            activities=planner_result[
                "activities"
            ],

            resource_report=planner_result[
                "resource_report"
            ],

            conflicts=planner_result[
                "conflicts"
            ],

            recommendations=planner_result[
                "recommendations"
            ],

            calendar=planner_result[
                "calendar"
            ],

            weather=planner_result[
                "weather"
            ],

            status="GENERATED"
        )

        # -------------------------------------------------
        # Step 4: Save the farm plan to the database.
        # -------------------------------------------------

        saved_plan = self.repository.create(
            model
        )

        # -------------------------------------------------
        # Step 5: Return the persisted farm plan.
        # -------------------------------------------------

        return saved_plan

    # =====================================================
    # CREATE
    # =====================================================

    def save_plan(
        self,
        plan: FarmPlanModel
    ):
        """
        Save a plan.
        """

        return self.repository.create(plan)

    # =====================================================
    # GET USER PLANS
    # =====================================================

    def get_all_plans(
        self,
        user_id: int
    ):
        """
        Retrieve all plans for a user.
        """

        return self.repository.get_all_by_user(
            user_id
        )

    # =====================================================
    # PAGINATION
    # =====================================================

    def get_paginated_plans(
        self,
        page: int,
        size: int
    ):
        """
        Paginated farm plans.
        """

        skip = (page - 1) * size

        plans = self.repository.get_paginated(
            skip=skip,
            limit=size
        )

        return {

            "page": page,

            "size": size,

            "total": self.repository.count(),

            "data": plans
        }

    # =====================================================
    # GET ONE
    # =====================================================

    def get_plan_by_id(
        self,
        plan_id: int
    ):
        return self.repository.get_by_id(
            plan_id
        )

    def get_user_plan(
        self,
        plan_id: int,
        user_id: int
    ):
        return self.repository.get_by_id_and_user(
            plan_id,
            user_id
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search_plans_by_crop(
        self,
        crop: str
    ):
        return self.repository.search_by_crop(
            crop
        )

    # =====================================================
    # FILTER
    # =====================================================

    def filter_plans_by_planting_date(
        self,
        planting_date: date
    ):
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
        Update any plan.
        """

        updated = self._serialize(
            request.model_dump()
        )

        updated["planting_date"] = (
            date.fromisoformat(
                updated["planting_date"]
            )
        )

        return self.repository.update(
            plan_id,
            updated
        )

    def update_user_plan(
        self,
        plan_id: int,
        user_id: int,
        request: FarmPlanUpdate
    ):
        """
        Update a user's own plan.
        """

        plan = self.repository.get_by_id_and_user(
            plan_id,
            user_id
        )

        if plan is None:
            return None

        updated = self._serialize(
            request.model_dump(
                exclude_unset=True
            )
        )

        if "planting_date" in updated:

            updated["planting_date"] = (
                date.fromisoformat(
                    updated["planting_date"]
                )
            )

        for key, value in updated.items():
            setattr(plan, key, value)

        return self.repository.save(plan)

    # =====================================================
    # DELETE
    # =====================================================

    def delete_plan(
        self,
        plan: FarmPlanModel
    ):
        return self.repository.delete(plan)

    def delete_user_plan(
        self,
        plan_id: int,
        user_id: int
    ):
        """
        Delete a user's own plan.
        """

        plan = self.repository.get_by_id_and_user(
            plan_id,
            user_id
        )

        if plan is None:
            return False

        self.repository.delete(plan)

        return True

    # =====================================================
    # STATISTICS
    # =====================================================

    def get_statistics(self):
        """
        Planner statistics.
        """

        return self.repository.get_statistics()