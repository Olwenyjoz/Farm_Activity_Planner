def detect_worker_conflicts(schedule, available_workers):
    """
    Detects worker conflicts by comparing the number of workers
    required for each day's activities with the number of workers
    available on the farm.
    """

    daily_schedule = {}

    conflicts = []

    # Group activities by date
    for activity in schedule["activities"]:

        date = activity["date"]

        if date not in daily_schedule:
            daily_schedule[date] = {
                "workers": 0,
                "activities": []
            }

        daily_schedule[date]["workers"] += activity["workers_required"]

        daily_schedule[date]["activities"].append(
            activity["name"]
        )

    # Detect conflicts
    for date, details in daily_schedule.items():

        if details["workers"] > available_workers:

            conflicts.append(
                {
                    "date": date,
                    "activities": details["activities"],
                    "workers_needed": details["workers"],
                    "workers_available": available_workers,
                    "worker_shortage": (
                        details["workers"] - available_workers
                    )
                }
            )

    return conflicts