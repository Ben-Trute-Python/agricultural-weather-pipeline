import sqlite3

DB_NAME = "hurricanes.db"

def init_db():
    """Creates the hurricane_records table if it doesn't already exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hurricane_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_name TEXT,
            latitude REAL,
            longitude REAL,
            date TEXT,
            max_wind_mph REAL,
            max_gusts_mph REAL,
            precipitation_inches REAL,
            wind_direction_deg REAL
        )
    """)
    conn.commit()
    conn.close()

def save_weather_reading(city_name, lat, lon, hurricane_data):
    """Parses Open-Meteo dictionary and saves rows into SQLite."""
    if not hurricane_data or "time" not in hurricane_data:
        return

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    dates = hurricane_data.get("time", [])
    winds = hurricane_data.get("wind_speed_10m_max", [])
    gusts = hurricane_data.get("wind_gusts_10m_max", [])
    rains = hurricane_data.get("precipitation_sum", [])
    dirs = hurricane_data.get("dominant_wind_direction_10m", [])

    for i in range(len(dates)):
        cursor.execute("""
            INSERT INTO hurricane_records 
            (city_name, latitude, longitude, date, max_wind_mph, max_gusts_mph, precipitation_inches, wind_direction_deg)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            city_name, lat, lon, 
            dates[i], 
            winds[i] if i < len(winds) else None,
            gusts[i] if i < len(gusts) else None,
            rains[i] if i < len(rains) else None,
            dirs[i] if i < len(dirs) else None
        ))

    conn.commit()
    conn.close()

# Ensure the database table exists as soon as database.py is imported
init_db()
