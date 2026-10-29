from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_DIR = PROJECT_DIR / "screenshots"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

state_file = INPUT_DIR / "sales_by_state.csv"
region_file = INPUT_DIR / "sales_by_region.csv"
if not state_file.exists() or not region_file.exists():
    raise FileNotFoundError(
        "Run python/02_analyze_sales.py first to create the processed CSV files."
    )

states = pd.read_csv(state_file)
regions = pd.read_csv(region_file)

top_states = states.nlargest(10, "Total_Sales").sort_values("Total_Sales")
plt.figure(figsize=(11, 7))
plt.barh(top_states["State"], top_states["Total_Sales"])
plt.title("Top 10 States by Total Sales")
plt.xlabel("Total sales")
plt.ylabel("State")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_10_states_sales.png", dpi=160)
plt.close()

regions = regions.sort_values("Total_Sales", ascending=False)
plt.figure(figsize=(9, 5))
plt.bar(regions["Region"], regions["Total_Sales"])
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_region.png", dpi=160)
plt.close()

plt.figure(figsize=(9, 5))
plt.bar(regions["Region"], regions["Total_Profit"])
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total profit")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "profit_by_region.png", dpi=160)
plt.close()

print("Charts saved in screenshots/:")
print("- top_10_states_sales.png")
print("- sales_by_region.png")
print("- profit_by_region.png")
