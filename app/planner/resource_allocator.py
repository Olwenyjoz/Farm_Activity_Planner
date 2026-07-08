def generate_resource_report(schedule):

    total_workers = 0

    equipment = []

    for activity in schedule["activities"]:

        total_workers += activity["workers_required"]

        equipment.extend(activity["equipment"])

    return {
        "total_workers_required": total_workers,
        "equipment_required": sorted(set(equipment))
    }