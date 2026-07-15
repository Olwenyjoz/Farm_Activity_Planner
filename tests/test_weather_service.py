"""
=========================================================
Module: test_weather_service.py

Purpose:
    Unit tests for the Weather Service.

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date

from app.planner.weather.service import get_weather_forecast


def test_weather_forecast():

    forecast = get_weather_forecast(
        date(2026, 8, 29)
    )

    assert forecast.condition == "Rain"

    assert forecast.rainfall_mm == 15

    assert forecast.temperature == 22