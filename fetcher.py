import urllib.request
import json

def get_weather_data(lat, lon):
    """
    Fetches 7-day weather forecast data from Open-Meteo API.
    Returns parsed JSON data, or None if the request fails.
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m"
        f"&daily=rain_sum"
        f"&temperature_unit=fahrenheit"
        f"&precipitation_unit=inch"
        f"&timezone=auto"
        f"&past_days=14"
    )
    
    try:
        print(f"🌐 Fetching weather data for coordinates ({lat}, {lon})...")
        response = urllib.request.urlopen(url, timeout=7)
        raw_data = response.read()
        return json.loads(raw_data)
        
    except Exception as network_error:
        print(f"⚠️ NETWORK CRISIS: Could not download data. Error: {network_error}")
        return None
