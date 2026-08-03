"""
=========================================================
Module: connection.py

Purpose:
    Configure the database connection.

Responsibilities:
    - Create the SQLAlchemy engine.
    - Configure the database connection.


=========================================================
"""

from sqlalchemy import create_engine

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False}
)