from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = PROJECT_DIR / "data" / "processed"
OUTPUT_DIR = INPUT_DIR
state_file = INPUT_DIR / "sales_by_state.csv"

if not state_file.exists():
    raise FileNotFoundError(
        "Run python/02_analyze_sales.py first to create sales_by_state.csv."
    )

states = pd.read_csv(state_file)
states["Sales_Rank"] = states["Total_Sales"].rank(
    ascending=False, method="dense"
).astype(int)
states["Profitability_Flag"] = states["Total_Profit"].apply(
    lambda value: "Positive profit" if value > 0 else "Zero or negative profit"
)
states["Interpretation"] = (
    "Historical sales indicator only; store coverage and local demand are unknown."
)

# High sales can indicate an established market, not necessarily an underserved one.
states = states.sort_values(["Total_Sales", "Total_Profit"], ascending=[False, False])
out = OUTPUT_DIR / "preliminary_expansion_screening.csv"
states.to_csv(out, index=False)

print("PRELIMINARY EXPANSION SCREENING")
print(states.head(10).to_string(index=False))
print(f"\nSaved: {out}")
print(
    "\nCaution: this analysis cannot identify underserved areas or prove a new "
    "store is warranted. To do that, add store locations/coverage and a demand "
    "measure such as population, customer counts, or local market size."
)
