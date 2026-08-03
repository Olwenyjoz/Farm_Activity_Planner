"""
=========================================================
Module: weather_client.py

Purpose:
    Communicate with the Open-Meteo Weather API.

Responsibilities:
    - Fetch weather forecasts.
    - Return raw weather data.

=========================================================
"""

import requests


class WeatherClient:
    """
    Client responsible for communicating with Open-Meteo.
    """

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(
        self,
        latitude: float,
        longitude: float
    ) -> dict:
        """
        Retrieve today's weather forecast.
        """

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "rain",
                "wind_speed_10m"
            ]
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()