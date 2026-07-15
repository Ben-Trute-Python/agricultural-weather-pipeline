# 🌾 Crop Requirements Database
CROP_PROFILES = {
    "fig": {
        "name": "Figs",
        "min_chill_hours": 100,
        "max_chill_hours": 300,
        "max_daily_rain": 1.5
    },
    "orange": {
        "name": "Cold-Hardy Citrus/Oranges",
        "min_chill_hours": 0,
        "max_chill_hours": 100,
        "max_daily_rain": 2.0
    },
    "pear": {
        "name": "Pears",
        "min_chill_hours": 200,
        "max_chill_hours": 600,
        "max_daily_rain": 1.2
    }
}

def evaluate_climate_match(weather_data, crop_key):
    """
    Calculates chill hours and peak rainfall from raw API data,
    and compares them against the specified crop's requirements.
    """
    if crop_key not in CROP_PROFILES:
        return None
        
    crop = CROP_PROFILES[crop_key]
    
    # 1. Calculate Chill Hours (hours where temperature is between 32°F and 45°F)
    hourly_temps = weather_data.get("hourly", {}).get("temperature_2m", [])
    chill_hours = sum(1 for temp in hourly_temps if 32 <= temp <= 45)
    
    # 2. Calculate Peak Daily Rainfall
    daily_rain = weather_data.get("daily", {}).get("rain_sum", [])
    max_rain = max(daily_rain) if daily_rain else 0.0
    
    # 3. Evaluate Match
    chill_match = crop["min_chill_hours"] <= chill_hours <= crop["max_chill_hours"]
    rain_match = max_rain <= crop["max_daily_rain"]
    is_compatible = chill_match and rain_match
    
    return {
        "compatible": is_compatible,
        "chill_hours": chill_hours,
        "max_rain": max_rain
    }
