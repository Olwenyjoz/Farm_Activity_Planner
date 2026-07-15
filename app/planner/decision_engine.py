"""
=========================================================
Module: decision_engine.py

Purpose:
    Generates intelligent recommendations for the
    Farm Activity Planner AI.

Responsibilities:
    - Analyze worker conflicts
    - Analyze workforce requirements
    - Analyze weather-sensitive activities
    - Analyze priority activities
    - Produce structured recommendations

Author:
    Deogracia Olweny
=========================================================
"""

from app.core.enums import (
    RecommendationSeverity,
    RecommendationCategory,
)

from app.core.constants import WORKFORCE_WARNING_THRESHOLD
from app.utils.text_utils import format_activity_list
from app.planner.weather.service import get_weather_forecast


def generate_recommendations(
    schedule,
    resource_report,
    conflicts,
):
    """
    Generate intelligent recommendations for the farm plan.

    Parameters
    ----------
    schedule : dict
        Generated farm schedule.

    resource_report : dict
        Resource allocation report.

    conflicts : list
        Worker conflicts detected.

    Returns
    -------
    list
        List of recommendation dictionaries.
    """

    recommendations = []

    # =====================================================
    # Rule 1: Worker Shortage
    # =====================================================
    for conflict in conflicts:

        activity_names = format_activity_list(
            conflict["activities"]
        )

        recommendations.append(
            {
                "title": "Worker Shortage",
                "category": RecommendationCategory.WORKERS.value,
                "severity": RecommendationSeverity.HIGH.value,
                "activity": activity_names,
                "date": conflict["date"],
                "reason": (
                    f"{activity_names} require(s) "
                    f"{conflict['workers_needed']} workers, "
                    f"but only {conflict['workers_available']} are available."
                ),
                "suggested_action": (
                    f"Hire {conflict['worker_shortage']} additional "
                    f"worker(s) or reschedule the affected activities."
                ),
            }
        )

    # =====================================================
    # Rule 2: Large Workforce Requirement
    # =====================================================
    if (
        resource_report["total_workers_required"]
        > WORKFORCE_WARNING_THRESHOLD
    ):

        recommendations.append(
            {
                "title": "Large Workforce Required",
                "category": RecommendationCategory.WORKERS.value,
                "severity": RecommendationSeverity.MEDIUM.value,
                "activity": "Farm Plan",
                "date": schedule["planting_date"],
                "reason": (
                    f"The farm plan requires "
                    f"{resource_report['total_workers_required']} "
                    f"worker assignments."
                ),
                "suggested_action": (
                    "Prepare sufficient labour before activities begin."
                ),
            }
        )

    # =====================================================
    # Rule 3 & Rule 4:
    # Weather + Priority
    # =====================================================
    for activity in schedule.get("activities", []):

        # ---------------------------------------------
        # Rule 3: Weather-Sensitive Activities
        # ---------------------------------------------
        if activity["weather_sensitive"]:

            forecast = get_weather_forecast(
                activity["date"]
            )

            # Heavy Rain
            if forecast.rainfall_mm >= 10:

                recommendations.append(
                    {
                        "title": "Heavy Rain Forecast",
                        "category": RecommendationCategory.WEATHER.value,
                        "severity": RecommendationSeverity.HIGH.value,
                        "activity": activity["name"],
                        "date": activity["date"],
                        "reason": (
                            f"{forecast.rainfall_mm} mm of rainfall "
                            f"is forecast."
                        ),
                        "suggested_action": (
                            "Postpone this activity until rainfall decreases."
                        ),
                    }
                )

            # Strong Wind
            elif forecast.wind_speed >= 15:

                recommendations.append(
                    {
                        "title": "Strong Wind Forecast",
                        "category": RecommendationCategory.WEATHER.value,
                        "severity": RecommendationSeverity.MEDIUM.value,
                        "activity": activity["name"],
                        "date": activity["date"],
                        "reason": (
                            f"Strong winds of "
                            f"{forecast.wind_speed} km/h "
                            f"are forecast."
                        ),
                        "suggested_action": (
                            "Avoid spraying during strong winds."
                        ),
                    }
                )

            # Suitable Weather
            else:

                recommendations.append(
                    {
                        "title": "Suitable Weather",
                        "category": RecommendationCategory.WEATHER.value,
                        "severity": RecommendationSeverity.LOW.value,
                        "activity": activity["name"],
                        "date": activity["date"],
                        "reason": (
                            f"{forecast.condition} weather "
                            f"is expected."
                        ),
                        "suggested_action": (
                            "Weather conditions are suitable "
                            "for the activity."
                        ),
                    }
                )

        # ---------------------------------------------
        # Rule 4: High Priority Activity
        # ---------------------------------------------
        if activity["priority"] == "High":

            recommendations.append(
                {
                    "title": "High Priority Activity",
                    "category": RecommendationCategory.PRIORITY.value,
                    "severity": RecommendationSeverity.HIGH.value,
                    "activity": activity["name"],
                    "date": activity["date"],
                    "reason": (
                        f"{activity['name']} is a high-priority "
                        "activity that should not be delayed."
                    ),
                    "suggested_action": (
                        "Prepare workers, equipment, transport "
                        "and required materials before the "
                        "scheduled date."
                    ),
                }
            )

    return recommendations