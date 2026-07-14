"""
=========================================================
Module: generator.py

Purpose:
    Generates calendar events from a farm activity
    schedule.

Responsibilities:
    - Transform activities into calendar events
    - Sort events chronologically
    - Provide reusable calendar data

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from typing import List


def generate_calendar(schedule: dict) -> List[dict]:
    """
    Generate calendar events from a farm schedule.

    Parameters
    ----------
    schedule : dict
        The generated farm schedule.

    Returns
    -------
    List[dict]
        A list of calendar event dictionaries.
    """

    # =====================================================
    # Store generated calendar events
    # =====================================================
    calendar_events = []

    # =====================================================
    # Transform activities into calendar events
    # =====================================================
    for activity in schedule.get("activities", []):

        calendar_events.append(
            {
                "title": activity["name"],
                "date": activity["date"],
                "priority": activity["priority"],
                "status": activity["status"],
            }
        )

    # =====================================================
    # Sort events chronologically
    # =====================================================
    calendar_events.sort(
        key=lambda event: event["date"]
    )

    return calendar_events