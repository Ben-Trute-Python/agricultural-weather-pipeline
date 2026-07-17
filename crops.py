# crops.py

CROP_DATABASE = {
    "Satsuma Mandarin": {
        "min_chill": 100,
        "max_hardiness_zone": 9,
        "min_rain_inches": 35,
        "hardiness_temp_f": 15,
        "notes": (
            "Extremely cold-hardy for a sweet orange (tolerates down to 15°F). "
            "Note: Active fruit will suffer damage if temperatures drop below 28°F "
            "or remain below freezing for a prolonged period without protection."
        )
    },
    "Changsha Mandarin": {
        "min_chill": 100,
        "max_hardiness_zone": 9,
        "min_rain_inches": 35,
        "hardiness_temp_f": 15,
        "notes": (
            "Highly cold-tolerant mandarin variety (down to 15°F). "
            "Fruit is vulnerable to damage below 28°F or during prolonged sub-freezing periods."
        )
    },
    "Other Sweet Citrus": {
        "min_chill": 100,
        "max_hardiness_zone": 9,
        "min_rain_inches": 35,
        "hardiness_temp_f": 20,
        "notes": (
            "Standard subtropical sweet citrus. Generally hardy to 20°F, "
            "but fruit damage occurs below 28°F or during prolonged freezing events."
        )
    },
    "Bosc Pear": {
        "min_chill": 800,
        "max_hardiness_zone": 8,
        "min_rain_inches": 30,
        "hardiness_temp_f": -10,  # Highly cold hardy
        "notes": "Requires significant winter chill to set fruit reliably."
    },
    "Celeste Fig": {
        "min_chill": 100,
        "max_hardiness_zone": 10,
        "min_rain_inches": 20,
        "hardiness_temp_f": 15,
        "notes": "Highly productive in hot, humid climates; low chill requirement."
    },
    "Italian Hazelnut": {
        "min_chill": 800,
        "max_hardiness_zone": 8,
        "min_rain_inches": 30,
        "hardiness_temp_f": -15,
        "notes": "Requires cross-pollination and adequate chilling hours."
    },
    "Apple": {
        "min_chill": 800,
        "max_hardiness_zone": 9,
        "min_rain_inches": 25,
        "hardiness_temp_f": -20,
        "notes": (
            "Standard apple cultivars prefer 800+ chill hours. However, "
            "recent research suggests that specific low-chill cultivars (like Anna or Ein Shemer) "
            "can be raised successfully below this threshold. Small-scale experimental plantings "
            "may be worth trying in borderline zones!"
        )
    }
}
