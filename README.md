# Texas Hurricane & Agricultural Weather Data Pipeline

An automated, resilient ETL (Extract, Transform, Load) pipeline built in Python to extract historical daily weather extremes (1950–present) across agricultural region centers in Texas. This system captures key meteorological factors—including peak wind gusts, precipitation totals, and prevailing wind vectors during major Gulf hurricane landfalls—storing structured metrics in SQLite for analytical modeling and structural planning.

---

## 🎯 Purpose & Agricultural Impact

Extreme weather events like hurricanes significantly impact regional farming, land management, and structural integrity. Beyond immediate crop damage, severe storms cause coastal storm surges, soil erosion, salt deposition, and catastrophic inland flooding that alter soil salinity and moisture profiles.

This pipeline provides a reproducible historical dataset designed to help producers, agronomists, architects, and researchers:
* **Optimized Windbreak Placement:** Analyze dominant historical storm vectors to strategically site windbreaks and shelterbelts, protecting vulnerable crop rows and topsoil from gale-force winds.
* **Structural Vulnerability & Wind Load Assessment:** Evaluate peak gust velocities and directional forces to determine reinforcement needs for farm buildings, greenhouses, and homes, or inform wind-load requirements for building architects.
* **Long-Term Orchard & Grove Siting:** Mitigate high-capital risks when planting perennial orchards and vineyards. Because tree crops require years of growth before returning to commercial fruit production, historical wind assessment prevents planting in high-risk zones where storm damage would cause multi-year losses.
* **Architectural & Civil Engineering Applications:** Provide building, residential, and landscape architects with localized severe-weather metrics to design resilient rural structures, select suitable structural fasteners, and plan wind-tolerant site layouts.
* **Correlate Weather Records with Yield Recovery:** Pair regional climate data with multi-year yield metrics to model post-storm agricultural recovery periods.

---

## 🏗️ Architecture & Pipeline Flow

The project separates data ingestion, database persistence, and analytical reporting into decoupled, modular scripts:

1. **Extraction (`hurricane.py`):** Fetches daily weather variables from the Open-Meteo Historical Weather API. Implements exponential backoff retries, explicit timeouts, and rate-limiting pauses to maintain connection stability under variable mobile network conditions.
2. **Configuration & Parameters (`config_hurricane.py` & `storms.py`):** Stores geographic target coordinates (lat/lon) for key Texas coastal/inland points and defines historical hurricane landfall date windows.
3. **Database Layer (`database.py`):** Manages SQLite connections, handles schema creation, and performs bulk upserts of weather observations.
4. **Data Reporting & Inspection (`view_data.py`):** Decoupled reporting module utilizing `pandas` to query SQLite and display clean tabular summaries or export formatted CSV files without making redundant API requests.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Data Processing:** Pandas
* **Database / Persistence:** SQLite3
* **HTTP Client & Resiliency:** Requests (3-attempt retry loop, status handling, 15-second timeout)
* **API Source:** Open-Meteo Historical Weather API

---

## 📊 Sample Output & Analysis Views

The pipeline transforms raw JSON payloads into structured, relational table entries containing:
* `city_name` (Target location)
* `date` (Landfall / event window)
* `max_wind_mph` (Peak 10m wind speed)
* `max_gusts_mph` (Maximum instantaneous wind gust)
* `precipitation_inches` (24-hour accumulation)
* `wind_direction_10m_dominant` (Dominant wind vector in degrees)

Using `view_data.py`, datasets can be formatted into pivot tables to compare storm severity across locations side-by-side:

| Date | Corpus Christi (Max Gust) | Port Aransas (Max Gust) | Precipitation (Avg in.) |
| :--- | :--- | :--- | :--- |
| **2017-08-25 (Harvey)** | 62.9 mph | 130.9 mph | 6.51 in |
| **2020-07-25 (Hanna)** | 52.3 mph | 88.1 mph | 2.73 in |

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ben-Trute-Python/agricultural-weather-pipeline.git](https://github.com/Ben-Trute-Python/agricultural-weather-pipeline.git)
   cd agricultural-weather-pipeline
   ```

2. **Execute the ETL Pipeline:**
   *(Extracts API metrics and populates `hurricanes.db`)*
   ```bash
   python hurricane.py
   ```

3. **Inspect the Results:**
   *(Queries SQLite database and outputs tabular data)*
   ```bash
   python view_data.py
   ```
