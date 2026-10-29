from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "raw"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

csv_files = list(DATA_DIR.glob("*.csv"))
if not csv_files:
    raise FileNotFoundError(f"No CSV found in {DATA_DIR}")

df = pd.read_csv(csv_files[0])
required = {"State", "Region", "Sales", "Profit", "Order Date"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")

for col in ["Sales", "Profit"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

state_sales = (
    df.groupby("State", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Record_Count=("Order Date", "count"),
    )
    .sort_values("Total_Sales", ascending=False)
)
region_sales = (
    df.groupby("Region", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Record_Count=("Order Date", "count"),
    )
    .sort_values("Total_Sales", ascending=False)
)

state_sales.to_csv(OUTPUT_DIR / "sales_by_state.csv", index=False)
region_sales.to_csv(OUTPUT_DIR / "sales_by_region.csv", index=False)

print("\nTOP 10 STATES BY SALES")
print(state_sales.head(10).to_string(index=False))
print("\nSALES BY REGION")
print(region_sales.to_string(index=False))
print(f"\nSaved results to {OUTPUT_DIR}")
