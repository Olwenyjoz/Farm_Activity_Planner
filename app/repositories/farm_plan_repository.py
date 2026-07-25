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

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
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
        """
        Initialize the repository with a database session.
        """
        self.db = db

    # =====================================================
    # CREATE
    # =====================================================

    def create(
        self,
        farm_plan: FarmPlanModel
    ):
        """
        Save a new farm plan to the database.
        """

        self.db.add(farm_plan)
        self.db.commit()
        self.db.refresh(farm_plan)

        return farm_plan

    # =====================================================
    # READ ALL
    # =====================================================

    def get_all(self):
        """
        Retrieve all farm plans.
        """

        return self.db.query(FarmPlanModel).all()

    # =====================================================
    # PAGINATED READ
    # =====================================================

    def get_paginated(
        self,
        skip: int,
        limit: int
    ):
        """
        Retrieve farm plans using pagination.
        """

        return (
            self.db.query(FarmPlanModel)
            .offset(skip)
            .limit(limit)
            .all()
        )

    # =====================================================
    # COUNT
    # =====================================================

    def count(self):
        """
        Return the total number of farm plans.
        """

        return (
            self.db.query(FarmPlanModel)
            .count()
        )

    # =====================================================
    # READ ONE
    # =====================================================

    def get_by_id(
        self,
        plan_id: int
    ):
        """
        Retrieve a farm plan by its ID.
        """

        return (
            self.db.query(FarmPlanModel)
            .filter(FarmPlanModel.id == plan_id)
            .first()
        )

    # =====================================================
    # SEARCH BY CROP
    # =====================================================

    def search_by_crop(
        self,
        crop: str
    ):
        """
        Search farm plans by crop name.
        """

        return (
            self.db.query(FarmPlanModel)
            .filter(
                FarmPlanModel.crop.ilike(f"%{crop}%")
            )
            .all()
        )

    # =====================================================
    # FILTER BY PLANTING DATE
    # =====================================================

    def filter_by_planting_date(
        self,
        planting_date: date
    ):
        """
        Retrieve farm plans by planting date.
        """

        return (
            self.db.query(FarmPlanModel)
            .filter(
                FarmPlanModel.planting_date == planting_date
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

        self.db.commit()
        self.db.refresh(plan)

        return plan

    # =====================================================
    # DELETE
    # =====================================================

    def delete(
        self,
        plan: FarmPlanModel
    ):
        """
        Delete a farm plan.
        """

        self.db.delete(plan)
        self.db.commit()

    # =====================================================
    # STATISTICS
    # =====================================================

    def get_statistics(self):
        """
        Retrieve summary statistics.
        """

        total_plans = self.count()

        crop_counts = (
            self.db.query(
                FarmPlanModel.crop,
                func.count(FarmPlanModel.id)
            )
            .group_by(FarmPlanModel.crop)
            .all()
        )

        return {
            "total_plans": total_plans,
            "crop_distribution": {
                crop: count
                for crop, count in crop_counts
            }
        }