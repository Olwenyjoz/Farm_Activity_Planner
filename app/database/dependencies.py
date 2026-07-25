"""
=========================================================
Module: dependencies.py

Purpose:
    Creates database sessions for FastAPI dependency
    injection.

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from app.database.session import SessionLocal


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()