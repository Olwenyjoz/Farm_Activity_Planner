"""
=========================================================
Module: service.py

Purpose:
    Provides calendar-related services for the
    Farm Activity Planner AI.

Responsibilities:
    - Generate calendar events
    - Coordinate calendar operations
    - Prepare for future integrations
      (ICS, Google Calendar, Outlook)

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from app.core.logger import logger
from app.planner.calendar.generator import generate_calendar


def build_calendar(schedule: dict) -> list[dict]:
    """
    Build calendar events from a farm schedule.

    Parameters
    ----------
    schedule : dict
        The generated farm schedule.

    Returns
    -------
    list[dict]
        Calendar events.
    """

    logger.info("Building farm calendar.")

    calendar_events = generate_calendar(schedule)

    logger.info(
        f"Built {len(calendar_events)} calendar event(s)."
    )

    return calendar_events