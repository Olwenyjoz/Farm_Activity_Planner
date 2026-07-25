"""
=========================================================
Module: session.py

Purpose:
    Configure SQLAlchemy database sessions.

Responsibilities:
    - Create database sessions.
    - Manage transactions.

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from sqlalchemy.orm import sessionmaker

from app.database.connection import engine


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)