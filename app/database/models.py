"""
=========================================================
Module: models.py

Purpose:
    Database models for the Farm Activity Planner AI.

Responsibilities:
    - Define ORM models.
    - Map Python objects to database tables.

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date

from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import JSON

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class FarmPlanModel(Base):
    """
    Farm plan database model.
    """

    __tablename__ = "farm_plans"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    crop: Mapped[str] = mapped_column(
        String(100)
    )

    planting_date: Mapped[date] = mapped_column(
        Date
    )

    activities: Mapped[list] = mapped_column(
        JSON
    )

    resource_report: Mapped[dict] = mapped_column(
        JSON
    )

    conflicts: Mapped[list] = mapped_column(
        JSON
    )

    recommendations: Mapped[list] = mapped_column(
        JSON
    )

    calendar: Mapped[list] = mapped_column(
        JSON
    )