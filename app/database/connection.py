"""
=========================================================
Module: connection.py

Purpose:
    Configure the database connection.

Responsibilities:
    - Create the SQLAlchemy engine.
    - Configure SQLite.

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///farm_planner.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)