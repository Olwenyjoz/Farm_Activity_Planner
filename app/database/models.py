"""
=========================================================
Module: models.py

Purpose:
    Database models for the Farm Activity Planner AI.

Responsibilities:
    - Define ORM models.
    - Map Python objects to database tables.

=========================================================
"""

from datetime import UTC
from datetime import date
from datetime import datetime

from sqlalchemy import (
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    JSON,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base


class FarmPlanModel(Base):
    """
    Database model representing a generated farm plan.
    """

    __tablename__ = "farm_plans"

    # =====================================================
    # PRIMARY KEY
    # =====================================================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    # =====================================================
    # OWNER
    # =====================================================

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    user = relationship(
        "User",
        back_populates="farm_plans"
    )

    # =====================================================
    # BASIC INFORMATION
    # =====================================================

    crop: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    planting_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    farm_size: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    workers: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    # =====================================================
    # FARM LOCATION
    # =====================================================

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    # =====================================================
    # GENERATED PLAN
    # =====================================================

    activities: Mapped[list] = mapped_column(
        JSON,
        nullable=False
    )

    resource_report: Mapped[dict] = mapped_column(
        JSON,
        nullable=False
    )

    conflicts: Mapped[list] = mapped_column(
        JSON,
        nullable=False
    )

    recommendations: Mapped[list] = mapped_column(
        JSON,
        nullable=False
    )

    calendar: Mapped[list] = mapped_column(
        JSON,
        nullable=False
    )

    # =====================================================
    # WEATHER
    # =====================================================

    weather: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
        default=dict
    )

    # =====================================================
    # PLAN STATUS
    # =====================================================

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="GENERATED"
    )

    # =====================================================
    # AUDIT INFORMATION
    # =====================================================

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
        nullable=False
    )