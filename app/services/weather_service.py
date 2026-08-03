"""
=========================================================
Module: weather_service.py

Purpose:
    Process weather information for farm planning.

Responsibilities:
    - Retrieve weather data.
    - Analyze planting conditions.
    - Generate weather recommendations.


=========================================================
"""

from app.clients.weather_client import WeatherClient


class WeatherService:
    """
    Service responsible for weather analysis.
    """

    def __init__(self):
        self.client = WeatherClient()

    def get_weather(
        self,
        latitude: float,
        longitude: float
    ):
        """
        Retrieve and analyze weather.
        """

        weather = self.client.get_weather(
            latitude,
            longitude
        )

        current = weather.get("current", {})

        temperature = current.get("temperature_2m")

        humidity = current.get(
            "relative_humidity_2m"
        )

        rain = current.get("rain")

        wind_speed = current.get(
            "wind_speed_10m"
        )

        recommendation = self.generate_recommendation(
            temperature,
            rain,
            wind_speed
        )

        return {
            "temperature": temperature,
            "humidity": humidity,
            "rain": rain,
            "wind_speed": wind_speed,
            "recommendation": recommendation
        }

    def generate_recommendation(
        self,
        temperature,
        rain,
        wind_speed
        ):
        """
        Generate a recommendation based on
        current weather.
        """

        rain = rain or 0
        wind_speed = wind_speed or 0
        temperature = temperature or 0

        if rain > 20:
            return (
                "Heavy rainfall expected. "
                "Delay planting."
            )

        if wind_speed > 30:
            return (
                "Strong winds detected. "
                "Avoid spraying."
            )

        if temperature > 35:
            return (
                "High temperatures expected. "
                "Increase irrigation."
            )

        return (
            "Weather conditions are suitable "
            "for farming activities."
        )