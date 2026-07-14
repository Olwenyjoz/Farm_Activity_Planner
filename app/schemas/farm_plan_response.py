from datetime import date
from pydantic import BaseModel

from app.schemas.calendar_event import CalendarEvent


class ActivityResponse(BaseModel):
    name: str
    date: date
    priority: str
    duration_hours: int
    workers_required: int
    equipment: list[str]
    description: str
    status: str
    weather_sensitive: bool


class ResourceReportResponse(BaseModel):
    total_workers_required: int
    equipment_required: list[str]


class ConflictResponse(BaseModel):
    date: date
    activities: list[str]
    workers_needed: int
    workers_available: int
    worker_shortage: int


class RecommendationResponse(BaseModel):
    title: str
    category: str
    severity: str
    activity: str
    date: date
    reason: str
    suggested_action: str


class FarmPlanResponse(BaseModel):
    crop: str
    planting_date: date
    activities: list[ActivityResponse]
    resource_report: ResourceReportResponse
    conflicts: list[ConflictResponse]
    recommendations: list[RecommendationResponse]
    calendar: list[CalendarEvent]