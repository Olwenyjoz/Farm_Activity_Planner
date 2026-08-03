"""
=========================================================
Module: farm_plan_repository.py

Purpose:
    Handles all database operations related to Farm Plans.

Responsibilities:
    - Create
    - Read
    - Update
    - Delete
    - Pagination
    - Search
    - Filtering
    - Statistics
    - User Ownership
    - Admin Queries


=========================================================
"""

from datetime import date

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.database.models import FarmPlanModel


class FarmPlanRepository:
    """
    Repository responsible for all Farm Plan
    database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    # =====================================================
    # CREATE
    # =====================================================

    def create(
        self,
        farm_plan: FarmPlanModel
    ) -> FarmPlanModel:
        """
        Save a new farm plan.
        """

        self.db.add(farm_plan)
        self.db.commit()
        self.db.refresh(farm_plan)

        return farm_plan

    # =====================================================
    # SAVE EXISTING OBJECT
    # =====================================================

    def save(
        self,
        farm_plan: FarmPlanModel
    ) -> FarmPlanModel:
        """
        Save changes made to an existing farm plan.
        """

        self.db.commit()
        self.db.refresh(farm_plan)

        return farm_plan

    # =====================================================
    # GET ALL (ADMIN)
    # =====================================================

    def get_all(self):
        """
        Retrieve every farm plan.
        """

        return (
            self.db.query(FarmPlanModel)
            .order_by(FarmPlanModel.created_at.desc())
            .all()
        )

    # =====================================================
    # GET USER PLANS
    # =====================================================

    def get_all_by_user(
        self,
        user_id: int
    ):
        """
        Retrieve all plans belonging to one user.
        """

        return (
            self.db.query(FarmPlanModel)
            .filter(
                FarmPlanModel.user_id == user_id
            )
            .order_by(
                FarmPlanModel.created_at.desc()
            )
            .all()
        )

    # =====================================================
    # GET BY ID
    # =====================================================

    def get_by_id(
        self,
        plan_id: int
    ):
        """
        Retrieve one plan by ID.
        """

        return (
            self.db.query(FarmPlanModel)
            .filter(
                FarmPlanModel.id == plan_id
            )
            .first()
        )

    # =====================================================
    # GET BY ID AND USER
    # =====================================================

    def get_by_id_and_user(
        self,
        plan_id: int,
        user_id: int
    ):
        """
        Retrieve one user's farm plan.
        """

        return (
            self.db.query(FarmPlanModel)
            .filter(
                FarmPlanModel.id == plan_id,
                FarmPlanModel.user_id == user_id
            )
            .first()
        )

    # =====================================================
    # PAGINATION
    # =====================================================

    def get_paginated(
        self,
        skip: int,
        limit: int
    ):
        """
        Retrieve paginated farm plans.
        """

        return (
            self.db.query(FarmPlanModel)
            .offset(skip)
            .limit(limit)
            .all()
        )

    # =====================================================
    # SEARCH
    # =====================================================

    def search_by_crop(
        self,
        crop: str
    ):
        """
        Search plans by crop.
        """

        return (
            self.db.query(FarmPlanModel)
            .filter(
                FarmPlanModel.crop.ilike(
                    f"%{crop}%"
                )
            )
            .all()
        )

    # =====================================================
    # FILTER
    # =====================================================

    def filter_by_planting_date(
        self,
        planting_date: date
    ):
        """
        Filter plans by planting date.
        """

        return (
            self.db.query(FarmPlanModel)
            .filter(
                FarmPlanModel.planting_date ==
                planting_date
            )
            .all()
        )

    # =====================================================
    # UPDATE
    # =====================================================

    def update(
        self,
        plan_id: int,
        updated_data: dict
    ):
        """
        Update an existing farm plan.
        """

        plan = self.get_by_id(plan_id)

        if plan is None:
            return None

        for key, value in updated_data.items():
            setattr(plan, key, value)

        return self.save(plan)

    # =====================================================
    # DELETE
    # =====================================================

    def delete(
        self,
        farm_plan: FarmPlanModel
    ):
        """
        Delete a farm plan.
        """

        self.db.delete(farm_plan)
        self.db.commit()

    # =====================================================
    # COUNT
    # =====================================================

    def count(self):
        """
        Return total farm plans.
        """

        return (
            self.db.query(FarmPlanModel)
            .count()
        )

    # =====================================================
    # USER COUNT
    # =====================================================

    def count_by_user(
        self,
        user_id: int
    ):
        """
        Count one user's plans.
        """

        return (
            self.db.query(FarmPlanModel)
            .filter(
                FarmPlanModel.user_id == user_id
            )
            .count()
        )

    # =====================================================
    # STATISTICS
    # =====================================================

    def get_statistics(self):
        """
        Return farm statistics.
        """

        total_plans = self.count()

        crop_distribution = (
            self.db.query(
                FarmPlanModel.crop,
                func.count(FarmPlanModel.id)
            )
            .group_by(
                FarmPlanModel.crop
            )
            .all()
        )

        return {
            "total_plans": total_plans,
            "crop_distribution": {
                crop: count
                for crop, count
                in crop_distribution
            }
        }