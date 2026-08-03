"""
=========================================================
Module: farm_plan_response.py

Purpose:
    Response schemas for Farm Activity Planner AI.

Responsibilities:
    - Define API response models
    - Serialize farm plan data
    - Support SQLAlchemy ORM model conversion


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

    model_config = ConfigDict(from_attributes=True)

    total_workers_required: int
    equipment_required: list[str]


# =====================================================
# CONFLICT RESPONSE
# =====================================================

class ConflictResponse(BaseModel):

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

    model_config = ConfigDict(from_attributes=True)

    title: str
    category: str
    severity: str
    activity: str
    date: date
    reason: str
    suggested_action: str


# =====================================================
# WEATHER RESPONSE
# =====================================================

class WeatherResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    temperature: float
    humidity: float
    rain: float
    wind_speed: float
    recommendation: str


# =====================================================
# FARM PLAN RESPONSE
# =====================================================

class FarmPlanResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int

    crop: str

    planting_date: date

    farm_size: float

    workers: int

    latitude: float

    longitude: float

    weather: WeatherResponse

    activities: list[ActivityResponse]

    resource_report: ResourceReportResponse

    conflicts: list[ConflictResponse]

    recommendations: list[RecommendationResponse]

    calendar: list[CalendarEvent]

    status: str