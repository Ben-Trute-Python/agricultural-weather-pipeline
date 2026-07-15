import matplotlib
# Forces Matplotlib to run in "headless" mode so it saves files without opening a window in Termux
matplotlib.use('Agg') 

import matplotlib.pyplot as plt
from datetime import datetime
import fetcher
import processor

# 📍 Regions to evaluate
TARGET_REGIONS = {
    "Houston": {"lat": 29.76, "lon": -95.36},
    "Corpus Christi": {"lat": 27.80, "lon": -97.40},
    "Miami": {"lat": 25.76, "lon": -80.19},
    "Chicago": {"lat": 41.87, "lon": -87.62}
}

def main():
    print("=== 🌾 Welcome to the Agricultural Pipeline Controller ===")
    print("Available crops: fig, orange, pear")
    selected_crop = input("Select a crop profile to evaluate: ").strip().lower()
    
    if selected_crop not in processor.CROP_PROFILES:
        print("❌ Invalid crop selection. Exiting.")
        return
        
    cities = []
    chill_results = []
    rain_results = []
    
    # Process each location
    for city, coords in TARGET_REGIONS.items():
        print(f"\nEvaluating: {city}")
        weather_report = fetcher.get_weather_data(coords["lat"], coords["lon"])
        
        if weather_report is None:
            print(f"⏩ Skipping evaluation for {city} due to connection failure.")
            continue
            
        evaluation = processor.evaluate_climate_match(weather_report, selected_crop)
        
        if evaluation:
            cities.append(city)
            chill_results.append(evaluation["chill_hours"])
            rain_results.append(evaluation["max_rain"])
            
            status = "🏆 MATCH" if evaluation["compatible"] else "❌ NO MATCH"
            print(f"Result for {city}: {status}")
            print(f" -> Chill Hours: {evaluation['chill_hours']} hrs")
            print(f" -> Peak Daily Rain: {evaluation['max_rain']:.2f} inches")
            
    if not cities:
        print("\n❌ No data was successfully processed. Dashboard generation canceled.")
        return

    # 📊 GENERATE AUTOMATED DASHBOARD
    print("\n📊 Creating visualization dashboard...")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
    
    crop_name = processor.CROP_PROFILES[selected_crop]["name"]
    fig.suptitle(f"Climate Suitability Analysis: {crop_name}", fontsize=16, fontweight='bold')
    
    # Top Subplot: Peak Daily Rainfall
    ax1.bar(cities, rain_results, color='royalblue', alpha=0.85)
    ax1.set_title("Peak Daily Rainfall")
    ax1.set_ylabel("Inches")
    ax1.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Bottom Subplot: Total Chill Hours
    ax2.bar(cities, chill_results, color='darkorange', alpha=0.85)
    ax2.set_title("Total Chill Hours")
    ax2.set_ylabel("Hours")
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    
    # 💾 Save Report with unique Timestamp
    current_time = datetime.now().strftime("%Y-%m-%d_%H%M")
    report_filename = f"climate_report_{selected_crop}_{current_time}.png"
    
    plt.savefig(report_filename, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\n💾 SUCCESS! Report successfully archived as: {report_filename}")

if __name__ == "__main__":
    main()
