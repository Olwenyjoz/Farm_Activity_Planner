"""
=========================================================
Module: base.py

Purpose:
    Defines the SQLAlchemy declarative base class.

Responsibilities:
    - Provide a base class for all database models.

=========================================================
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all ORM models.
    """
    pass