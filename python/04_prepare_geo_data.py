from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"

state_file = INPUT_DIR / "sales_by_state.csv"
if not state_file.exists():
    raise FileNotFoundError(
        "Run python/02_analyze_sales.py first to create sales_by_state.csv."
    )

states = pd.read_csv(state_file)
# The source has state names but no coordinates or geometry.
# This script creates a tidy table ready to join with a verified geographic boundary file.
states["State"] = states["State"].astype(str).str.strip()
states.to_csv(OUTPUT_DIR / "state_sales_for_mapping.csv", index=False)

print(f"Prepared {len(states)} state-level records.")
print(f"Saved: {OUTPUT_DIR / 'state_sales_for_mapping.csv'}")
print(
    "\nNote: this file is not itself a map. A verified state-boundary GeoJSON "
    "or shapefile is needed for a choropleth map."
)
