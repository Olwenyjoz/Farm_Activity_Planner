from datetime import timedelta

CROP_RULES = {

    "Maize": {
        
        "activities": [
        {
            "name": "First Weeding",
            "offset": timedelta(days=21),
            "priority": "High",
            "duration_hours": 5,
            "workers_required": 4,
            "equipment": [
                "Hoe"
            ],
            "description": "Remove weeds around young maize plants.",
            "status": "Planned",
            "weather_sensitive": False
        },
        {
            "name": "Fertilizer Application",
            "offset": timedelta(days=30),
            "priority": "High",
            "duration_hours": 3,
            "workers_required": 3,
            "equipment": [
                "Fertilizer",
                "Protective Gloves"
            ],
            "description": "Apply fertilizer to support healthy crop growth.",
            "status": "Planned",
            "weather_sensitive": False
        },
        {
            "name": "Spraying",
            "offset": timedelta(days=45),
            "priority": "Medium",
            "duration_hours": 2,
            "workers_required": 2,
            "equipment": [
                "Knapsack Sprayer",
                "Protective Clothing"
            ],
            "description": "Spray approved pesticide to control pests.",
            "status": "Planned",
            "weather_sensitive": True
        },
        {
            "name": "Harvest",
            "offset": timedelta(days=120),
            "priority": "High",
            "duration_hours": 8,
            "workers_required": 6,
            "equipment": [
                "Harvest Bags",
                "Wheelbarrow"
            ],
            "description": "Harvest mature maize and transport it for storage.",
            "status": "Planned",
            "weather_sensitive": True
        }
    ]
},

    "Beans": {

        "activities": [

            {
                "name": "First Weeding",
                "offset": timedelta(days=14)
            },

            {
                "name": "Harvest",
                "offset": timedelta(days=90)
            }

        ]

    }

}