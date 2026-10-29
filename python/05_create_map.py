
from pathlib import Path

import pandas as pd
import folium
import json

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# File locations
SALES_FILE = PROJECT_DIR / "data" / "processed" / "state_sales_for_mapping.csv"
GEOJSON_FILE = PROJECT_DIR / "data" / "raw" / "us-states.json"
MAP_FILE = PROJECT_DIR / "maps" / "sales_map.html"

# Load sales data and state boundaries
sales = pd.read_csv(SALES_FILE)

with open(GEOJSON_FILE, "r", encoding="utf-8") as file:
    states_geojson = json.load(file)

# Standardize state names before matching
sales["State"] = sales["State"].astype(str).str.strip()

# Check which GeoJSON property contains the state name
first_feature = states_geojson["features"][0]
print("GeoJSON properties:", first_feature["properties"])

# Create the map
sales_map = folium.Map(
    location=[39.5, -98.35],
    zoom_start=4,
    tiles="OpenStreetMap"
)

# Add a sales-by-state color layer
folium.Choropleth(
    geo_data=states_geojson,
    data=sales,
    columns=["State", "Total_Sales"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.75,
    line_opacity=0.2,
    legend_name="Total Sales by State (USD)",
    highlight=True
).add_to(sales_map)

# Add state names and sales values in popups/tooltips

# Match sales values to the state boundaries
sales_lookup = sales.set_index("State")["Total_Sales"].to_dict()

for feature in states_geojson["features"]:
    state_name = feature["properties"]["name"]
    total_sales = sales_lookup.get(state_name)

    feature["properties"]["total_sales"] = (
        f"${total_sales:,.2f}" if total_sales is not None
        else "No sales data"
    )

folium.GeoJson(
    states_geojson,
    name="State details",
    style_function=lambda feature: {
        "color": "#555555",
        "weight": 0.6,
        "fillOpacity": 0
    },
    tooltip=folium.GeoJsonTooltip(
        fields=["name", "total_sales"],
        aliases=["State:", "Total Sales:"]
    )
).add_to(sales_map)


folium.LayerControl().add_to(sales_map)

# Save the map
MAP_FILE.parent.mkdir(parents=True, exist_ok=True)
sales_map.save(str(MAP_FILE))

print(f"Interactive sales map saved to: {MAP_FILE}")
