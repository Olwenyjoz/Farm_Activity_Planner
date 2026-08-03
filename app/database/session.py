"""
=========================================================
Module: session.py

Purpose:
    Configure SQLAlchemy database sessions.

Responsibilities:
    - Create database sessions.
    - Manage transactions.


=========================================================
"""

from sqlalchemy.orm import sessionmaker

from app.database.connection import engine

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)