"""
=========================================================
Database model registration.

Purpose:
    Import all ORM models so SQLAlchemy registers them
    before Base.metadata.create_all() is executed.
=========================================================
"""

from app.database.models import FarmPlanModel
from app.models.user import User

__all__ = [
    "FarmPlanModel",
    "User",
]