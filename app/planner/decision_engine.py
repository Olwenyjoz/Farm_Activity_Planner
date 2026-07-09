def generate_recommendations(schedule, resource_report, conflicts):

    recommendations = []

    if conflicts:

        recommendations.append(
            "Worker shortage detected. Consider hiring temporary workers or rescheduling activities."
        )

    return recommendations