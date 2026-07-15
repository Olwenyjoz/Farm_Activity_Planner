"""
=========================================================
Module: test_calendar_service.py

Purpose:
    Unit tests for the Calendar Service.

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date

from app.planner.calendar.service import build_calendar


def test_build_calendar_returns_sorted_events():
    """
    Verify that the calendar service returns events
    sorted by date.
    """

    schedule = {
        "activities": [
            {
                "name": "Harvest",
                "date": date(2026, 11, 12),
                "priority": "High",
                "status": "Planned",
            },
            {
                "name": "Planting",
                "date": date(2026, 7, 15),
                "priority": "High",
                "status": "Planned",
            },
        ]
    }

    calendar = build_calendar(schedule)

    assert len(calendar) == 2

    assert calendar[0]["title"] == "Planting"

    assert calendar[1]["title"] == "Harvest"