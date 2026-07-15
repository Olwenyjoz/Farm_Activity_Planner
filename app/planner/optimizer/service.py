"""
=========================================================
Module: service.py

Purpose:
    Optimizes generated farm schedules.

Responsibilities:
    - Improve activity scheduling
    - Reduce weather-related risks
    - Produce an optimized schedule

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import timedelta

from app.core.logger import logger
from app.planner.weather.service import get_weather_forecast


def optimize_schedule(schedule: dict) -> dict:
    """
    Optimize a generated farm schedule.

    Parameters
    ----------
    schedule : dict
        Generated farm schedule.

    Returns
    -------
    dict
        Optimized schedule.
    """

    logger.info("Optimizing farm schedule.")

    # Work on a copy of the schedule
    optimized_schedule = schedule.copy()

    for activity in optimized_schedule["activities"]:

        # Skip activities that are not weather-sensitive
        if not activity["weather_sensitive"]:
            continue

        forecast = get_weather_forecast(
            activity["date"]
        )

        # -------------------------------------------------
    # Rule:
    # Find the next suitable weather day
    # -------------------------------------------------

    if forecast.rainfall_mm >= 10:

        old_date = activity["date"]
        new_date = old_date

        # Search for a suitable weather day
        search_days = 0

        while search_days < 7:

            new_date += timedelta(days=1)
            search_days += 1

            next_forecast = get_weather_forecast(new_date)

            if (
                next_forecast.rainfall_mm < 10
                and next_forecast.wind_speed < 15
            ):
                break

        activity["date"] = new_date

        logger.info(
            f"{activity['name']} moved "
            f"from {old_date} to {new_date}"
        )
        
    return optimized_schedule