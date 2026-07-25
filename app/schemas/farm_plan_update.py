"""
=========================================================
Module: farm_plan_update.py

Purpose:
    Request schema for updating a farm plan.

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date

from pydantic import BaseModel


class FarmPlanUpdate(BaseModel):
    """
    User input allowed when updating a farm plan.
    """

    crop: str
    planting_date: date
    farm_size: float
    workers: int