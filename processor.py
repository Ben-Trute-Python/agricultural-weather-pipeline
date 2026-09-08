# 🌾 Crop Requirements Database
from crops import CROP_DATABASE
def evaluate_climate_match(weather_data, crop_key):
    """
    Calculates climate metrics from raw API data and compares them
    against the single source of truth in CROP_DATABASE.
    """
    # 1. Guardrail: Make sure the crop exists in your crops.py file
    if crop_key not in CROP_DATABASE:
        return None
        
    crop_specs = CROP_DATABASE[crop_key]

    # 2. Calculate Chill Hours from raw weather data
    hourly_temps = weather_data.get("hourly", {}).get("temperature_2m", [])
    chill_hours = sum(1 for temp in hourly_temps if 32 <= temp <= 45)

    # 3. Calculate Daily Peak Rainfall
    daily_rain = weather_data.get("daily", {}).get("rain_sum", [])
    max_rain = max(daily_rain) if daily_rain else 0.0

    # 4. Evaluate the Match using your EXACT crops.py keys!
    # (Note: We use crop_specs["min_chill"] here!)
    chill_ok = chill_hours >= crop_specs.get("min_chill", 0)
    
    # If you want to check rain against max_daily_rain:
    rain_ok = max_rain <= crop_specs.get("min_daily_rain", 99.0) 

    # Determine absolute compatibility
    is_compatible = chill_ok and rain_ok

    return {
        "compatible": is_compatible,
        "chill_hours": chill_hours,
        "max_rain": max_rain
    }
