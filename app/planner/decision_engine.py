def generate_recommendations(schedule, resource_report, conflicts):
    """
    Generates intelligent recommendations based on:
    1. Worker conflicts
    2. Resource requirements
    3. Activity priority
    4. Weather-sensitive activities
    """

    recommendations = []

    # --------------------------------------------------------
    # Rule 1: Worker Shortage
    # --------------------------------------------------------
    for conflict in conflicts:

        activity_names = ", ".join(conflict["activities"])

        recommendations.append(
            {
                "title": "Worker Shortage",
                "category": "Workers",
                "severity": "High",
                "activity": activity_names,
                "date": conflict["date"],
                "reason": (
                    f"{activity_names} require(s) "
                    f"{conflict['workers_needed']} workers, "
                    f"but only {conflict['workers_available']} are available."
                ),
                "suggested_action": (
                    f"Hire {conflict['worker_shortage']} additional worker(s) "
                    f"or reschedule the affected activities."
                ),
            }
        )

    # --------------------------------------------------------
    # Rule 2: Large Workforce Requirement
    # --------------------------------------------------------
    if resource_report["total_workers_required"] > 20:

        recommendations.append(
            {
                "title": "Large Workforce Required",
                "category": "Workers",
                "severity": "Medium",
                "activity": "Farm Plan",
                "date": schedule["planting_date"],
                "reason": (
                    f"The farm plan requires "
                    f"{resource_report['total_workers_required']} worker assignments."
                ),
                "suggested_action": (
                    "Prepare sufficient labor before activities begin."
                ),
            }
        )

    # --------------------------------------------------------
    # Rule 3 & Rule 4
    # --------------------------------------------------------
    for activity in schedule.get("activities", []):

    # Rule 3: Weather-sensitive activity
        if activity["weather_sensitive"]:

            recommendations.append(
                {
                    "title": "Weather Monitoring",
                    "category": "Weather",
                    "severity": "Medium",
                    "activity": activity["name"],
                    "date": activity["date"],
                    "reason": (
                        f"{activity['name']} is weather-sensitive and may be affected by rainfall or strong winds."
                    ),
                    "suggested_action": (
                        "Review the weather forecast 24 hours before the scheduled activity and postpone if conditions are unsuitable."
                    ),
                }
            )

    # Rule 4: High-priority activity
        if activity["priority"] == "High":

            recommendations.append(
                {
                    "title": "High Priority Activity",
                    "category": "Priority",
                    "severity": "High",
                    "activity": activity["name"],
                    "date": activity["date"],
                    "reason": (
                        f"{activity['name']} is a high-priority activity that should not be delayed."
                    ),
                    "suggested_action": (
                        "Prepare workers, equipment, transport, and required materials before the scheduled date."
                    ),
                }
            )
            
    return recommendations