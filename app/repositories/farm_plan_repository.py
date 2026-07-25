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

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from sqlalchemy.orm import Session
from app.database.models import FarmPlanModel


class FarmPlanRepository:

    def __init__(self, db: Session):
        self.db = db

    # =====================================================
    # CREATE
    # =====================================================

    def create(self, farm_plan: FarmPlanModel):

        self.db.add(farm_plan)

        self.db.commit()

        self.db.refresh(farm_plan)

        return farm_plan

    # =====================================================
    # READ ALL
    # =====================================================

    def get_all(self):

        return self.db.query(FarmPlanModel).all()

    # =====================================================
    # READ ONE
    # =====================================================

    def get_by_id(self, plan_id: int):

        return (
            self.db.query(FarmPlanModel)
            .filter(FarmPlanModel.id == plan_id)
            .first()
        )

    # =====================================================
    # UPDATE
    # =====================================================

    def update(self, farm_plan: FarmPlanModel):

        self.db.commit()

        self.db.refresh(farm_plan)

        return farm_plan

    # =====================================================
    # DELETE
    # =====================================================

    def delete(self, farm_plan: FarmPlanModel):

        self.db.delete(farm_plan)

        self.db.commit()