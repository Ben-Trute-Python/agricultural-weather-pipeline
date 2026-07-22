# crops.py

CROP_DATABASE = {
    "Satsuma Mandarin": {
        "min_chill": 100,
        "usda_zone": "8b",
        "hardiness_temp_f": 15,  # Hardy to 15F
        "min_rain_inches": 35,
        "notes": (
            "Extremely cold-hardy for a sweet orange (tolerates down to 15°F). "
            "Note: Active fruit will suffer damage if temperatures drop below 28°F "
            "or remain below freezing for a prolonged period without protection."
        )
    },
    "Changsha Mandarin": {
        "min_chill": 100,
        "usda_zone": "8b",
        "hardiness_temp_f": 15,  # Hardy to 15F
        "min_rain_inches": 35,
        "notes": (
            "Highly cold-tolerant mandarin variety (down to 15°F). "
            "Fruit is vulnerable to damage below 28°F or during prolonged sub-freezing periods."
        )
    },
    "Other Sweet Citrus": {
        "min_chill": 100,
        "usda_zone": "9a",
        "hardiness_temp_f": 20,  # Standard citrus limit
        "min_rain_inches": 35,
        "notes": (
            "Standard subtropical sweet citrus. Generally hardy to 20°F (Zone 9a), "
            "but fruit damage occurs below 28°F or during prolonged freezing events."
        )
    },
    "Bosc Pear": {
        "min_chill": 800,
        "usda_zone": "8a",
        "hardiness_temp_f": 10,
        "min_rain_inches": 30,
        "notes": "Requires significant winter chill to set fruit reliably."
    },
    "Celeste Fig": {
        "min_chill": 100,
        "usda_zone": "8b",
        "hardiness_temp_f": 15,
        "min_rain_inches": 20,
        "notes": "Highly productive in hot, humid climates; low chill requirement."
    },
    "Italian Hazelnut": {
        "min_chill": 600,  # Updated to correct 600 hour minimum!
        "usda_zone": "8a",
        "hardiness_temp_f": 10,
        "min_rain_inches": 30,
        "notes": "Vigorous tree with relatively low chill requirements well suited to areas with mild winters."
    },
    "Apple": {
        "min_chill": 800,
        "usda_zone": "9a",
        "hardiness_temp_f": 20,
        "min_rain_inches": 25,
        "notes": (
            "Standard apple cultivars prefer 800+ chill hours. However, "
            "recent research suggests that specific low-chill cultivars (like Anna or Ein Shemer) "
            "can be raised successfully below this threshold. Small-scale experimental plantings "
            "may be worth trying in borderline zones!"
        )
    },
    "Sour Cherries": {  
        "min_chill": 800,
        "usda_zone": "3", 
        "hardiness_temp_f": -40,  # Hardy
        "min_rain_inches": 25,
        "notes": (
           "Extremely cold-hardy"
           "Note: Sour Cherries tolorate colder tempatures than sweet cherries but require more chill hours also" 
       )        
    },
    "Low Chill Sweet Cherries": {
        "min_chill": 300,
        "usda_zone": "5",
        "hardiness_temp_f": -20,
        "min_rain_inches": 25,
        "notes": "Requires well-drained soil."
    },
    "Medium Chill Sweet Cherries": {
        "min_chill": 500,
        "usda_zone": "5",
        "hardiness_temp_f": -20,
        "min_rain_inches": 25,
        "notes": "Requires well-drained soil."
    },
    "Hass Avacado": {
        "min_chill": 0,
        "usda_zone": "9",
        "hardiness_temp_f": 20,
        "min_rain_inches": 40,
        "notes": "Many avacados especialy west indiand types are not well adapted to freezing tempratures. This data only appplys to Hass or a few other hardy varieties."
    },
    "All In One Almond": {
        "min_chill": 300,
        "usda_zone": "5",
        "hardiness_temp_f": -20,
        "min_rain_inches": 40,
        "notes": " Most almonds require 300 chill hours. However, different almond varieties may have slightly different chilling requirements. For example, some sources suggest that Nonpareil almonds need more chill hours (400-600). Therefore, it is important to know the specific chilling requirement of your almond variety before planting or managing your orchard."
    }
}   
