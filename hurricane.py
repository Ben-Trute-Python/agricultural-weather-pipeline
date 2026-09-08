import requests
from confighurricane import TEXAS_CITIES
from storms import TEXAS_HURRICANES
import database
import time

def fetch_hurricane_weather(city_name, lat, lon, start_date, end_date):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        # Updated: wind_direction_10m_dominant
        "daily": "wind_speed_10m_max,wind_gusts_10m_max,precipitation_sum,wind_direction_10m_dominant",
        "wind_speed_unit": "mph",
        "precipitation_unit": "inch",
        "timezone": "auto"
    }
    for attempt in range(3):
        try:
            response = requests.get(url, params=params, timeout=15)

            if response.status_code == 200:
                hurricane_data = response.json().get("daily", {})
                if hurricane_data:
                    database.save_weather_reading(city_name, lat, lon, hurricane_data)
                    return hurricane_data
            elif response.status_code == 429:
                print("Rate limit reached. Waiting 2 seconds...")
                time.sleep(2)
            else:
                print(f"API Error ({response.status_code}): {response.text}")

        except requests.exceptions.RequestException as e:
            if attempt == 2:
                print(f"Network call failed after 3 attempts: {e}")
            time.sleep(1)

    return {}

def run_analysis():
    # Iterates automatically over whichever cities are NOT commented out in config.py
    for city_name, coords in TEXAS_CITIES.items():
        print(f"\n==========================================")
        print(f"  Fetching Hurricane Data for: {city_name}")
        print(f"==========================================")
        
        for storm in TEXAS_HURRICANES:
            storm_name = storm["name"]
            landfall_date = storm["date"]
            
            weather_data = fetch_hurricane_weather(
                city_name=city_name,
                lat=coords["lat"],
                lon=coords["lon"],
                start_date=landfall_date,
                end_date=landfall_date
            )
            time.sleep(0.2)            
            # Print or log output
            print(f"{storm_name} ({landfall_date}): {weather_data}")

if __name__ == "__main__":
    run_analysis()
