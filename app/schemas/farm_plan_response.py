"""
=========================================================
Module: farm_plan_response.py

Purpose:
    Response schemas for Farm Activity Planner AI.

Responsibilities:
    - Define API response models
    - Serialize farm plan data
    - Support SQLAlchemy ORM model conversion

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date

from pydantic import BaseModel
from pydantic import ConfigDict

from app.schemas.calendar_event import CalendarEvent


# =====================================================
# ACTIVITY RESPONSE
# =====================================================

class ActivityResponse(BaseModel):
    """
    Represents a scheduled farm activity.
    """

    model_config = ConfigDict(from_attributes=True)

    name: str
    date: date
    priority: str
    duration_hours: int
    workers_required: int
    equipment: list[str]
    description: str
    status: str
    weather_sensitive: bool


# =====================================================
# RESOURCE REPORT RESPONSE
# =====================================================

class ResourceReportResponse(BaseModel):
    """
    Summary of required farm resources.
    """

    model_config = ConfigDict(from_attributes=True)

    total_workers_required: int
    equipment_required: list[str]


# =====================================================
# CONFLICT RESPONSE
# =====================================================

class ConflictResponse(BaseModel):
    """
    Represents scheduling conflicts.
    """

    model_config = ConfigDict(from_attributes=True)

    date: date
    activities: list[str]
    workers_needed: int
    workers_available: int
    worker_shortage: int


# =====================================================
# RECOMMENDATION RESPONSE
# =====================================================

class RecommendationResponse(BaseModel):
    """
    Planner recommendations.
    """

    model_config = ConfigDict(from_attributes=True)

    title: str
    category: str
    severity: str
    activity: str
    date: date
    reason: str
    suggested_action: str


# =====================================================
# FARM PLAN RESPONSE
# =====================================================

class FarmPlanResponse(BaseModel):
    """
    Complete farm plan returned by the API.
    """

    model_config = ConfigDict(from_attributes=True)

    id: int

    crop: str
    planting_date: date

    activities: list[ActivityResponse]

    resource_report: ResourceReportResponse

    conflicts: list[ConflictResponse]

    recommendations: list[RecommendationResponse]

    calendar: list[CalendarEvent]