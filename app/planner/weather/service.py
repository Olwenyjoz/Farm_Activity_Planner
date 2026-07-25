"""
=========================================================
Module: service.py

Purpose:
    Provides weather forecasting services for the
    Farm Activity Planner AI.

Responsibilities:
    - Retrieve weather forecasts
    - Simulate seasonal weather during development
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
    Retrieve a simulated weather forecast.

    During development this function generates
    realistic seasonal weather based on the month.
    """

    logger.info(
        f"Retrieving weather forecast for {forecast_date}."
    )

    month = forecast_date.month

    # =====================================================
    # Seasonal Weather Simulation
    # =====================================================

    if month in (1, 2):
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Sunny",
            temperature=31,
            wind_speed=8,
            rainfall_mm=0,
        )

    elif month in (3,):
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Light Rain",
            temperature=28,
            wind_speed=12,
            rainfall_mm=8,
        )

    elif month in (4, 5):
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Heavy Rain",
            temperature=24,
            wind_speed=18,
            rainfall_mm=40,
        )

    elif month == 6:
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Cloudy",
            temperature=23,
            wind_speed=10,
            rainfall_mm=5,
        )

    elif month == 7:
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Cool",
            temperature=21,
            wind_speed=9,
            rainfall_mm=2,
        )

    elif month == 8:
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Sunny",
            temperature=27,
            wind_speed=10,
            rainfall_mm=0,
        )

    elif month == 9:
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Light Rain",
            temperature=26,
            wind_speed=12,
            rainfall_mm=10,
        )

    elif month == 10:
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Rain",
            temperature=24,
            wind_speed=14,
            rainfall_mm=20,
        )

    elif month == 11:
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Cloudy",
            temperature=24,
            wind_speed=8,
            rainfall_mm=2,
        )

    else:  # December
        forecast = WeatherForecast(
            date=forecast_date,
            condition="Sunny",
            temperature=30,
            wind_speed=8,
            rainfall_mm=0,
        )

    logger.info(
        f"Weather forecast retrieved: {forecast.condition}"
    )

    return forecast