"""
=========================================================
Module: test_calendar_generator.py

Purpose:
    Test the Calendar Generator module independently.

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date

from app.planner.calendar.generator import generate_calendar


def main():
    """
    Run a simple manual test for the calendar generator.
    """

    schedule = {
        "crop": "Maize",
        "planting_date": date(2026, 7, 15),
        "activities": [
            {
                "name": "Harvest",
                "date": date(2026, 11, 12),
                "priority": "High",
                "status": "Planned",
            },
            {
                "name": "First Weeding",
                "date": date(2026, 8, 5),
                "priority": "High",
                "status": "Planned",
            },
            {
                "name": "Spraying",
                "date": date(2026, 8, 29),
                "priority": "Medium",
                "status": "Planned",
            },
        ],
    }

    calendar = generate_calendar(schedule)

    print("\nGenerated Calendar Events\n")

    for event in calendar:
        print(event)


if __name__ == "__main__":
    main()