"""
=========================================================
Module: calendar_event.py

Purpose:
    Defines the response schema for calendar events.

Responsibilities:
    - Validate calendar event data
    - Standardize API responses
    - Improve documentation

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date

from pydantic import BaseModel


class CalendarEvent(BaseModel):
    """
    Represents a farm calendar event.
    """

    title: str
    date: date
    priority: str
    status: str