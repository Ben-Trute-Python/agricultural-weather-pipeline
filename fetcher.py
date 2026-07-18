import urllib.request
import json

def get_weather_data(lat, lon, start_date, end_date):
    """
    Fetches historical weather data for a specific winter block 
    from the Open-Meteo Archive API.
    """
    # 🔄 We switch from /v1/forecast to /v1/archive to allow historical queries
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={lon}"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
        f"&hourly=temperature_2m"
        f"&daily=rain_sum"
        f"&temperature_unit=fahrenheit"
        f"&precipitation_unit=inch"
        f"&timezone=auto"
    )

    try:
        # The rest of your network code stays exactly the same!
        print(f"🌍 Fetching data from API...")
        response = urllib.request.urlopen(url, timeout=7)
        raw_data = response.read()
        return json.loads(raw_data)
        
    except Exception as network_error:
        print(f"⚠️ NETWORK CRISIS: Could not download data. Error: {network_error}")
        return None
