from datetime import timedelta

CROP_RULES = {
    "Maize": {
        "first_weeding": timedelta(days=21),
        "harvest": timedelta(days=120),
    },

    "Beans": {
        "first_weeding": timedelta(days=14),
        "harvest": timedelta(days=90),
    },

    "Rice": {
        "first_weeding": timedelta(days=30),
        "harvest": timedelta(days=150),
    }
}