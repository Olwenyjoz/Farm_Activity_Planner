from datetime import date
from pydantic import BaseModel


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
    workers_needed: int
    workers_available: int


class FarmPlanResponse(BaseModel):
    crop: str
    planting_date: date
    activities: list[ActivityResponse]
    resource_report: ResourceReportResponse
    conflicts: list[ConflictResponse]