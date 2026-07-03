from pydantic import BaseModel
from datetime import date


class FarmPlanRequest(BaseModel):
    crop: str
    planting_date: date
    farm_size: float
    workers: int