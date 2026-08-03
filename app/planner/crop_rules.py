"""
=========================================================
Module: crop_rules.py

Purpose:
    Crop activity knowledge base for the
    Farm Activity Planner AI.

Responsibilities:
    - Define activity timelines.
    - Define worker requirements.
    - Define equipment requirements.
    - Define activity priorities.
    - Define weather sensitivity.
    - Provide planning rules for supported crops.
    
=========================================================
"""

from datetime import timedelta

CROP_RULES = {

    # =====================================================
    # MAIZE
    # =====================================================

    "Maize": {

        "activities": [

            {
                "name": "Land Preparation",

                "offset": timedelta(days=-14),

                "priority": "High",

                "duration_hours": 8,

                "workers_required": 6,

                "equipment": [
                    "Tractor",
                    "Plough"
                ],

                "description":
                    "Prepare land before planting.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Planting",

                "offset": timedelta(days=0),

                "priority": "High",

                "duration_hours": 6,

                "workers_required": 5,

                "equipment": [
                    "Seeds",
                    "Hoe"
                ],

                "description":
                    "Plant certified maize seeds.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "First Weeding",

                "offset": timedelta(days=21),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 4,

                "equipment": [
                    "Hoe"
                ],

                "description":
                    "Remove weeds around maize.",

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

                "description":
                    "Top-dress maize with fertilizer.",

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
                    "Knapsack Sprayer"
                ],

                "description":
                    "Spray against pests.",

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

                "description":
                    "Harvest mature maize.",

                "status": "Planned",

                "weather_sensitive": True
            }

        ]

    },

    # =====================================================
    # BEANS
    # =====================================================

    "Beans": {

        "activities": [

            {
                "name": "Land Preparation",

                "offset": timedelta(days=-7),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 4,

                "equipment": [
                    "Hoe"
                ],

                "description":
                    "Prepare land for beans.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Planting",

                "offset": timedelta(days=0),

                "priority": "High",

                "duration_hours": 4,

                "workers_required": 3,

                "equipment": [
                    "Bean Seeds"
                ],

                "description":
                    "Plant bean seeds.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "First Weeding",

                "offset": timedelta(days=14),

                "priority": "High",

                "duration_hours": 3,

                "workers_required": 2,

                "equipment": [
                    "Hoe"
                ],

                "description":
                    "Remove weeds.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Flowering Inspection",

                "offset": timedelta(days=35),

                "priority": "Medium",

                "duration_hours": 2,

                "workers_required": 2,

                "equipment": [
                    "Notebook"
                ],

                "description":
                    "Inspect flowering stage.",

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
                    "Knapsack Sprayer"
                ],

                "description":
                    "Control pests and diseases.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Harvest",

                "offset": timedelta(days=90),

                "priority": "High",

                "duration_hours": 6,

                "workers_required": 5,

                "equipment": [
                    "Harvest Bags"
                ],

                "description":
                    "Harvest mature beans.",

                "status": "Planned",

                "weather_sensitive": True
            }

        ]

    },

    # =====================================================
    # TOMATO
    # =====================================================

    "Tomato": {

        "activities": [

            {
                "name": "Nursery Preparation",

                "offset": timedelta(days=-30),

                "priority": "High",

                "duration_hours": 6,

                "workers_required": 3,

                "equipment": [
                    "Seed Trays"
                ],

                "description":
                    "Prepare tomato nursery.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Transplanting",

                "offset": timedelta(days=0),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 4,

                "equipment": [
                    "Seedlings"
                ],

                "description":
                    "Transplant seedlings to the field.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Staking",

                "offset": timedelta(days=21),

                "priority": "Medium",

                "duration_hours": 4,

                "workers_required": 3,

                "equipment": [
                    "Wooden Stakes",
                    "Twine"
                ],

                "description":
                    "Support tomato plants.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Spraying",

                "offset": timedelta(days=35),

                "priority": "High",

                "duration_hours": 3,

                "workers_required": 2,

                "equipment": [
                    "Knapsack Sprayer"
                ],

                "description":
                    "Control tomato diseases.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Harvest",

                "offset": timedelta(days=90),

                "priority": "High",

                "duration_hours": 8,

                "workers_required": 5,

                "equipment": [
                    "Harvest Crates"
                ],

                "description":
                    "Harvest ripe tomatoes.",

                "status": "Planned",

                "weather_sensitive": False
            }

        ]

    },
        # =====================================================
    # POTATO
    # =====================================================

    "Potato": {

        "activities": [

            {
                "name": "Land Preparation",

                "offset": timedelta(days=-14),

                "priority": "High",

                "duration_hours": 8,

                "workers_required": 5,

                "equipment": [
                    "Tractor",
                    "Plough"
                ],

                "description":
                    "Prepare the field for potato planting.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Planting",

                "offset": timedelta(days=0),

                "priority": "High",

                "duration_hours": 6,

                "workers_required": 5,

                "equipment": [
                    "Seed Potatoes"
                ],

                "description":
                    "Plant certified seed potatoes.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Earthing Up",

                "offset": timedelta(days=28),

                "priority": "High",

                "duration_hours": 4,

                "workers_required": 4,

                "equipment": [
                    "Hoe"
                ],

                "description":
                    "Heap soil around potato stems.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Disease Control",

                "offset": timedelta(days=45),

                "priority": "Medium",

                "duration_hours": 3,

                "workers_required": 2,

                "equipment": [
                    "Knapsack Sprayer"
                ],

                "description":
                    "Control late blight and pests.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Harvest",

                "offset": timedelta(days=110),

                "priority": "High",

                "duration_hours": 8,

                "workers_required": 6,

                "equipment": [
                    "Harvest Bags"
                ],

                "description":
                    "Harvest mature potatoes.",

                "status": "Planned",

                "weather_sensitive": False
            }

        ]

    },

    # =====================================================
    # COFFEE
    # =====================================================

    "Coffee": {

        "activities": [

            {
                "name": "Pruning",

                "offset": timedelta(days=7),

                "priority": "Medium",

                "duration_hours": 6,

                "workers_required": 4,

                "equipment": [
                    "Pruning Shears"
                ],

                "description":
                    "Remove old and damaged branches.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Fertilizer Application",

                "offset": timedelta(days=30),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 3,

                "equipment": [
                    "Fertilizer"
                ],

                "description":
                    "Apply fertilizer around coffee trees.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Pest Monitoring",

                "offset": timedelta(days=45),

                "priority": "Medium",

                "duration_hours": 3,

                "workers_required": 2,

                "equipment": [
                    "Inspection Kit"
                ],

                "description":
                    "Inspect coffee trees for pests.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Spraying",

                "offset": timedelta(days=60),

                "priority": "Medium",

                "duration_hours": 3,

                "workers_required": 2,

                "equipment": [
                    "Knapsack Sprayer"
                ],

                "description":
                    "Spray fungicides when necessary.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Harvest",

                "offset": timedelta(days=240),

                "priority": "High",

                "duration_hours": 10,

                "workers_required": 8,

                "equipment": [
                    "Harvest Baskets"
                ],

                "description":
                    "Harvest ripe coffee cherries.",

                "status": "Planned",

                "weather_sensitive": False
            }

        ]

    },

    # =====================================================
    # RICE
    # =====================================================

    "Rice": {

        "activities": [

            {
                "name": "Field Preparation",

                "offset": timedelta(days=-10),

                "priority": "High",

                "duration_hours": 8,

                "workers_required": 6,

                "equipment": [
                    "Tractor"
                ],

                "description":
                    "Prepare rice field.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Transplanting",

                "offset": timedelta(days=0),

                "priority": "High",

                "duration_hours": 8,

                "workers_required": 8,

                "equipment": [
                    "Rice Seedlings"
                ],

                "description":
                    "Transplant rice seedlings.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Water Management",

                "offset": timedelta(days=20),

                "priority": "High",

                "duration_hours": 2,

                "workers_required": 2,

                "equipment": [
                    "Water Gates"
                ],

                "description":
                    "Maintain appropriate water level.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Weeding",

                "offset": timedelta(days=35),

                "priority": "Medium",

                "duration_hours": 5,

                "workers_required": 4,

                "equipment": [
                    "Hoe"
                ],

                "description":
                    "Remove weeds from the paddy.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Harvest",

                "offset": timedelta(days=135),

                "priority": "High",

                "duration_hours": 10,

                "workers_required": 8,

                "equipment": [
                    "Harvest Bags"
                ],

                "description":
                    "Harvest mature rice.",

                "status": "Planned",

                "weather_sensitive": False
            }

        ]

    },
        # =====================================================
    # SUNFLOWER
    # =====================================================

    "Sunflower": {

        "activities": [

            {
                "name": "Land Preparation",

                "offset": timedelta(days=-10),

                "priority": "High",

                "duration_hours": 6,

                "workers_required": 4,

                "equipment": [
                    "Tractor",
                    "Plough"
                ],

                "description":
                    "Prepare land for sunflower planting.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Planting",

                "offset": timedelta(days=0),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 4,

                "equipment": [
                    "Sunflower Seeds"
                ],

                "description":
                    "Plant sunflower seeds.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Weeding",

                "offset": timedelta(days=21),

                "priority": "Medium",

                "duration_hours": 4,

                "workers_required": 3,

                "equipment": [
                    "Hoe"
                ],

                "description":
                    "Remove weeds around sunflower plants.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Harvest",

                "offset": timedelta(days=120),

                "priority": "High",

                "duration_hours": 8,

                "workers_required": 5,

                "equipment": [
                    "Harvest Bags"
                ],

                "description":
                    "Harvest mature sunflower heads.",

                "status": "Planned",

                "weather_sensitive": False
            }

        ]

    },

    # =====================================================
    # SORGHUM
    # =====================================================

    "Sorghum": {

        "activities": [

            {
                "name": "Land Preparation",

                "offset": timedelta(days=-10),

                "priority": "High",

                "duration_hours": 6,

                "workers_required": 4,

                "equipment": [
                    "Plough"
                ],

                "description":
                    "Prepare the land for sorghum.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Planting",

                "offset": timedelta(days=0),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 4,

                "equipment": [
                    "Sorghum Seeds"
                ],

                "description":
                    "Plant sorghum seeds.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Weeding",

                "offset": timedelta(days=25),

                "priority": "Medium",

                "duration_hours": 4,

                "workers_required": 3,

                "equipment": [
                    "Hoe"
                ],

                "description":
                    "Control weeds.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Harvest",

                "offset": timedelta(days=115),

                "priority": "High",

                "duration_hours": 8,

                "workers_required": 5,

                "equipment": [
                    "Harvest Bags"
                ],

                "description":
                    "Harvest mature sorghum.",

                "status": "Planned",

                "weather_sensitive": False
            }

        ]

    },

    # =====================================================
    # CABBAGE
    # =====================================================

    "Cabbage": {

        "activities": [

            {
                "name": "Nursery Preparation",

                "offset": timedelta(days=-30),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 3,

                "equipment": [
                    "Seed Trays"
                ],

                "description":
                    "Prepare cabbage nursery.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Transplanting",

                "offset": timedelta(days=0),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 4,

                "equipment": [
                    "Seedlings"
                ],

                "description":
                    "Transplant seedlings into the field.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Top Dressing",

                "offset": timedelta(days=30),

                "priority": "Medium",

                "duration_hours": 3,

                "workers_required": 2,

                "equipment": [
                    "Fertilizer"
                ],

                "description":
                    "Apply fertilizer.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Harvest",

                "offset": timedelta(days=90),

                "priority": "High",

                "duration_hours": 6,

                "workers_required": 5,

                "equipment": [
                    "Harvest Crates"
                ],

                "description":
                    "Harvest mature cabbage.",

                "status": "Planned",

                "weather_sensitive": False
            }

        ]

    },

    # =====================================================
    # ONION
    # =====================================================

    "Onion": {

        "activities": [

            {
                "name": "Nursery Preparation",

                "offset": timedelta(days=-35),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 3,

                "equipment": [
                    "Seed Trays"
                ],

                "description":
                    "Prepare onion nursery.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Transplanting",

                "offset": timedelta(days=0),

                "priority": "High",

                "duration_hours": 5,

                "workers_required": 4,

                "equipment": [
                    "Seedlings"
                ],

                "description":
                    "Transplant onion seedlings.",

                "status": "Planned",

                "weather_sensitive": True
            },

            {
                "name": "Irrigation",

                "offset": timedelta(days=20),

                "priority": "Medium",

                "duration_hours": 2,

                "workers_required": 2,

                "equipment": [
                    "Irrigation Kit"
                ],

                "description":
                    "Water onion crop.",

                "status": "Planned",

                "weather_sensitive": False
            },

            {
                "name": "Harvest",

                "offset": timedelta(days=120),

                "priority": "High",

                "duration_hours": 8,

                "workers_required": 6,

                "equipment": [
                    "Harvest Bags"
                ],

                "description":
                    "Harvest mature onions.",

                "status": "Planned",

                "weather_sensitive": False
            }

        ]

    }

}