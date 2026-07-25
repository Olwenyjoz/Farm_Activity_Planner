"""
=========================================================
Module: farm_plan_create.py

Purpose:
    Request schema for creating a farm plan.

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date

from pydantic import BaseModel


class FarmPlanCreate(BaseModel):
    """
    User input required to generate a farm plan.
    """

    crop: str
    planting_date: date
    farm_size: float
    workers: int