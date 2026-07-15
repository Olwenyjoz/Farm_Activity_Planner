"""
=========================================================
Module: service.py

Purpose:
    Provides weather forecasting services for the
    Farm Activity Planner AI.

Responsibilities:
    - Retrieve weather forecasts
    - Simulate weather data during development
    - Provide a single access point for weather
      information

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from datetime import date

from app.core.logger import logger
from app.planner.weather.models import WeatherForecast


def get_weather_forecast(
    forecast_date: date,
) -> WeatherForecast:
    """
    Retrieve a weather forecast for a given date.

    During development this function returns
    simulated weather data.

    Parameters
    ----------
    forecast_date : date

    Returns
    -------
    WeatherForecast
    """

    logger.info(
        f"Retrieving weather forecast for {forecast_date}."
    )

    # =====================================================
    # Simulated Weather Conditions
    # =====================================================

    weather_data = {

        date(2026, 8, 5): WeatherForecast(
            date=date(2026, 8, 5),
            condition="Sunny",
            temperature=28,
            wind_speed=10,
            rainfall_mm=0,
        ),

        date(2026, 8, 14): WeatherForecast(
            date=date(2026, 8, 14),
            condition="Cloudy",
            temperature=25,
            wind_speed=12,
            rainfall_mm=2,
        ),

        date(2026, 8, 29): WeatherForecast(
            date=date(2026, 8, 29),
            condition="Rain",
            temperature=22,
            wind_speed=18,
            rainfall_mm=15,
        ),

        date(2026, 11, 12): WeatherForecast(
            date=date(2026, 11, 12),
            condition="Cloudy",
            temperature=24,
            wind_speed=8,
            rainfall_mm=1,
        ),
    }

    forecast = weather_data.get(
        forecast_date,

        WeatherForecast(
        date=forecast_date,
        condition="Unknown",
        temperature=0,
        wind_speed=100,
        rainfall_mm=100,
        )
    )

    logger.info(
        f"Weather forecast retrieved: {forecast.condition}"
    )

    return forecast