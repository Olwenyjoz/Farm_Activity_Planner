"""
=========================================================
Module: farm_plan.py

Purpose:
    Defines the internal Farm Plan domain model.

Responsibilities:
    - Represent a farm plan within the application
    - Encapsulate farm planning data
    - Provide a strongly typed internal model

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from dataclasses import dataclass, field
from datetime import date


@dataclass
class FarmPlan:
    """
    Internal representation of a generated farm plan.
    """

    crop: str

    planting_date: date

    activities: list = field(default_factory=list)

    resource_report: dict = field(default_factory=dict)

    conflicts: list = field(default_factory=list)

    recommendations: list = field(default_factory=list)

    calendar: list = field(default_factory=list)