"""
=========================================================
Module: models.py

Purpose:
    Defines weather-related domain models used by the
    Farm Activity Planner AI.

Responsibilities:
    - Represent weather forecasts
    - Standardize weather information
    - Provide strongly typed weather objects

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class WeatherForecast:
    """
    Represents the weather forecast for a single day.
    """

    date: date

    condition: str

    temperature: float

    wind_speed: float

    rainfall_mm: float