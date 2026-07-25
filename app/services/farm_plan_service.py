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


class FarmPlanService:
    """
    Service layer responsible for coordinating business
    logic between the API and the database.
    """

    def __init__(self, repository: FarmPlanRepository):
        """
        Initialize the service with a repository instance.

        Parameters
        ----------
        repository : FarmPlanRepository
            Repository responsible for database operations.
        """
        self.repository = repository


    #Serialization of date
    def _serialize_for_database(self, data):
        """
        Recursively convert Python objects into JSON-serializable values.
        """

        if isinstance(data, dict):
            return {
                key: self._serialize_for_database(value)
                for key, value in data.items()
            }

        elif isinstance(data, list):
            return [
                self._serialize_for_database(item)
                for item in data
            ]

        elif isinstance(data, date):
            return data.isoformat()

        elif isinstance(data, timedelta):
            return data.days

        return data
        
    # =====================================================
    # GENERATE FARM PLAN
    # =====================================================

    def generate_plan(self, request):
        """
        Generate a farm plan, save it to the database,
        then return the generated response.

        Parameters
        ----------
        request : FarmPlanRequest
            The validated farm planning request.

        Returns
        -------
        dict
            The generated farm plan.
        """

        # Generate the farm schedule
        result = generate_schedule(request)
        
        print(hasattr(self, "_serialize_for_database"))
        print(dir(self))
    
        db_result = self._serialize_for_database(result)

        # Convert the generated dictionary into
        # a SQLAlchemy model for database storage.
        model = FarmPlanModel(
            crop=db_result["crop"],
            planting_date=date.fromisoformat(db_result["planting_date"]),
            activities=db_result["activities"],
            resource_report=db_result["resource_report"],
            conflicts=db_result["conflicts"],
            recommendations=db_result["recommendations"],
            calendar=db_result["calendar"]
        )

        # Save the farm plan
        self.repository.create(model)

        # Return the generated plan
        return result

    # =====================================================
    # CREATE
    # =====================================================

    def save_plan(self, plan: FarmPlanModel):
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
    # READ ONE
    # =====================================================

    def get_plan(self, plan_id: int):
        """
        Retrieve a farm plan by its ID.
        """
        return self.repository.get_by_id(plan_id)

    # =====================================================
    # UPDATE
    # =====================================================

    def update_plan(self, plan: FarmPlanModel):
        """
        Update an existing farm plan.
        """
        return self.repository.update(plan)

    # =====================================================
    # DELETE
    # =====================================================

    def delete_plan(self, plan: FarmPlanModel):
        """
        Delete a farm plan.
        """
        self.repository.delete(plan)