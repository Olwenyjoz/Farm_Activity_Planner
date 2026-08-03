"""
=========================================================
Module: dependencies.py

Purpose:
    Creates database sessions for FastAPI dependency
    injection.


=========================================================
"""

from app.database.session import SessionLocal


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()