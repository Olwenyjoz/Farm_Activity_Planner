def detect_worker_conflicts(schedule, available_workers):

    daily_workers = {}

    conflicts = []

    for activity in schedule["activities"]:

        date = activity["date"]

        workers = activity["workers_required"]

        daily_workers[date] = daily_workers.get(date, 0) + workers

    for date, workers in daily_workers.items():

        if workers > available_workers:

            conflicts.append(
                {
                    "date": date,
                    "workers_needed": workers,
                    "workers_available": available_workers
                }
            )

    return conflicts