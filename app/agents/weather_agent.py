"""
=========================================================
Module: weather_agent.py

Purpose:
    Weather Intelligence Agent.

Responsibilities:
    - Coordinate weather analysis.
    - Retrieve current weather conditions.
    - Produce weather intelligence.
    - Return structured weather information.


=========================================================
"""

from app.services.weather_service import WeatherService


class WeatherAgent:
    """
    AI agent responsible for weather analysis.
    """

    def __init__(self):
        """
        Initialize the Weather Service.
        """

        self.weather_service = WeatherService()

    # =====================================================
    # ANALYZE WEATHER
    # =====================================================

    def analyze(
        self,
        latitude: float,
        longitude: float
    ):
        """
        Analyze current weather conditions.

        Workflow:
            1. Receive farm coordinates.
            2. Retrieve weather data.
            3. Return weather intelligence.
        """

        weather = self.weather_service.get_weather(

            latitude=latitude,

            longitude=longitude
        )

        return weather