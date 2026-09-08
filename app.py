# app.py
import sys
import os
import fetcher
import processor
import datetime
from crops import CROP_DATABASE

TARGET_REGIONS = {
    "Houston": {"lat": 29.76, "lon": -95.36},
    "Corpus Christi": {"lat": 27.8, "lon": -97.4},
    "Galveston": {"lat": 29.3013, "lon": -94.7977},
    "Houston Bush": {"lat": 29.9802, "lon": -95.3397},
    "Beaumont": {"lat": 30.0802, "lon": -94.1275},
    "Victoria": {"lat": 28.8053, "lon": -97.0036},
    "Laredo": {"lat": 27.5036, "lon": -99.4821},
    "Brownsville": {"lat": 25.9018, "lon": -97.4975},
    "McAllen": {"lat": 26.2034, "lon": -98.2300},
    "Del Rio": {"lat": 29.3627, "lon": -100.8968},
    "Tyler": {"lat": 32.3513, "lon": -95.3011},
    "Lufkin": {"lat": 31.3382, "lon": -94.7291},
    "Texarkana": {"lat": 33.4251, "lon": -94.0477},
    "College Station": {"lat": 30.6280, "lon": -96.3344},
    "Austin Camp Mabry": {"lat": 30.3121, "lon": -97.7656},
    "San Antonio": {"lat": 29.4241, "lon": -98.4936},
    "Kerrville": {"lat": 30.0474, "lon": -99.1403},
    "Llano": {"lat": 30.7593, "lon": -98.6750}
}

def get_user_crop_selection():
    """Displays a numbered menu and captures multiple crop selections."""
    print("\n⚡=== Welcome to the Agricultural Pipeline Controller ===")
    print("Available crops in database:")
    
    crop_list = list(CROP_DATABASE.keys())
    for index, crop_name in enumerate(crop_list, start=1):
        print(f"  [{index}] {crop_name}")
        
    print("=======================================================")
    user_input = input("Select multiple crops by number, separated by commas (e.g., 1,2,5): ")
    
    selected_crops = []
    try:
        choices = [int(x.strip()) for x in user_input.split(",") if x.strip()]
        for choice in choices:
            if 1 <= choice <= len(crop_list):
                selected_crops.append(crop_list[choice - 1])
            else:
                print(f"⚠️ Warning: Choice {choice} is out of range. Skipping.")
    except ValueError:
        print("❌ Error: Invalid input formatting. Numbers and commas only.")
        sys.exit(1)
        
    if not selected_crops:
        print("❌ Error: No valid crops selected. Exiting.")
        sys.exit(1)
        
    return selected_crops

def main():
    # 1. Get chosen crops from user
    selected_crops = get_user_crop_selection()
    print(f"\nEvaluating system suitability for collective orchard: {', '.join(selected_crops)}\n")
    
    perfect_match_count = 0
    apple_warnings = []

    # 2. Loop through our cleaned-up Texas regions
    # 2. Loop through our cleaned-up Texas regions
    for city, coords in TARGET_REGIONS.items():
        print(f"Evaluating: {city}")
        
        # 🗓️ Calculate dynamic winter dates (Oct 1 of last year to April 30 of this year)
        current_year = datetime.datetime.now().year
        start_date = f"{current_year - 1}-10-01"
        end_date = f"{current_year}-04-30"
        
        print(f"📡 Fetching historical winter data ({start_date} to {end_date})...")
        
        # # 1. This calls your live API fetcher file
        raw_data = fetcher.get_weather_data(coords['lat'], coords['lon'], start_date=start_date, end_date=end_date)
        # 2. This calls your processor file to crunch the data
        
        # 3. LINK THE LIVE METRICS HERE (Replacing my placeholders!)
        
        # Track if this city works for ALL selected crops
        city_is_suitable_for_all = True
        
       # Track if this city works for ALL selected crops
        city_is_suitable_for_all = True
            
        for crop in selected_crops:
        # 1. Run the processor tool
            weather_metrics = processor.evaluate_climate_match(raw_data, crop)
                
            # 2. Get the results from processor.py
            chill_hours = weather_metrics['chill_hours']
            peak_rain = weather_metrics['max_rain']     
            is_compatible = weather_metrics['compatible'] 
                
            # 3. Pull our database specifications for Apple logic
            specs = CROP_DATABASE[crop]
                
            # 4. If the processor says it's NOT compatible
            if not is_compatible:
            # Check for our special Apple research exception
                if crop == "Apple" and peak_rain <= specs["min_rain_inches"]:
                    apple_warnings.append(f"  -> {city}: {specs['notes']}")
                else:
                    # Otherwise, it's a hard fail for this city
                    city_is_suitable_for_all = False
                    break

        # 3. Print the collective verdict for this city
        if city_is_suitable_for_all:
            print(f"Result for {city}: ✅ MATCH FOUND FOR ALL SELECTED CROPS")
            perfect_match_count += 1
        else:
            print(f"Result for {city}: ❌ NO MATCH")
            
        print(f"  -> Chill Hours: {chill_hours} hrs")
        print(f"  -> Calculated Rain: {peak_rain} inches\n")

    # 4. Final Summary Verdict Block
    print("="*55)
    print("FINAL REGIONAL SYNTHESIS REPORT")
    print("="*55)
    if perfect_match_count == 0:
        print("❌ CRITICAL: No single region evaluated meets the baseline criteria")
        print("   for all selected fruits/nuts simultaneously.")
    else:
        print(f"🎉 SUCCESS: Found {perfect_match_count} region(s) capable of supporting")
        print("   your collective perennial custom orchard configuration.")
        
    # Print the conditional apple research notes if relevant
    if apple_warnings:
        print("\n🍎 RESEARCH EXCEPTION NOTES FOR APPLES:")
        for warning in apple_warnings:
            print(warning)
    print("="*55)

    # --- YOUR EXISTING GRAPH DASHBOARD CODE ---
    # Keep your tail end visualization pipeline intact right here!

if __name__ == "__main__":
    main()
