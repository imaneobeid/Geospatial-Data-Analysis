# Geospatial Data Analysis: Retail Sales and Expansion Screening

## Project Overview

This project analyzes geographic patterns in the Sample Superstore retail sales dataset. It uses Python to compare sales and profit across US states and regions, visualize sales performance, and create an interactive geographic sales map.

The project also includes a preliminary expansion-screening analysis to identify strong sales markets and highlight the additional information needed to evaluate potential new store locations.

## Objectives

- Inspect and validate the sales dataset.
- Compare total sales and profit across states and regions.
- Visualize the top-performing states and regional performance.
- Create an interactive choropleth map showing total sales by US state.
- Display state names and sales values through interactive map tooltips.
- Screen historical sales performance to support further expansion research.
- Document the limitations of the available data and identify additional requirements for reliable store-location decisions.

## Dataset

The project uses the Sample Superstore sales dataset, containing 9,994 records and 9 columns.

The dataset includes:

- Order Date
- Region
- State
- Category
- Sub-Category
- Segment
- Sales
- Profit
- Quantity

The dataset contains no missing values in these columns.

**Important data limitation:** The source dataset does not include store coordinates, customer coordinates, population, customer density, or existing store locations.

Place the CSV file in `data/raw/`. The inspection script reads the CSV file from this folder.

## Tools and Technologies

- **Python** — data analysis and automation
- **pandas** — data cleaning, aggregation, and analysis
- **Matplotlib** — charts and data visualization
- **Folium** — interactive geographic mapping
- **GeoJSON** — US state boundary data
- **GeoPandas** — available for future geospatial analysis
- **Visual Studio Code** — development environment

## Project Structure

```text
Geospatial-Data-Analysis/
├── data/
│   ├── raw/
│   │   ├── superstore_sales.csv
│   │   └── us-states.json
│   └── processed/
│       ├── sales_by_state.csv
│       ├── sales_by_region.csv
│       ├── state_sales_for_mapping.csv
│       └── preliminary_expansion_screening.csv
├── maps/
│   └── sales_map.html
├── python/
│   ├── 01_inspect_data.py
│   ├── 02_analyze_sales.py
│   ├── 03_visualize_sales.py
│   ├── 04_prepare_geo_data.py
│   ├── 05_create_map.py
│   └── 06_expansion_analysis.py
├── screenshots/
│   ├── top_10_states_sales.png
│   ├── sales_by_region.png
│   └── profit_by_region.png
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup and Installation

Create and activate a virtual environment, then install the required dependencies.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Ensure that the sales CSV is in `data/raw/` and the US state boundary file is saved as `data/raw/us-states.json`.

## How to Run

Run the following commands from the project root directory:

```powershell
python python/01_inspect_data.py
python python/02_analyze_sales.py
python python/03_visualize_sales.py
python python/04_prepare_geo_data.py
python python/05_create_map.py
python python/06_expansion_analysis.py
```

## Analysis and Visualizations

### 1. Data Inspection

The dataset contains 9,994 records and 9 columns. The initial inspection found no missing values in the supplied columns.

### 2. State-Level Sales Analysis

The ten highest-sales states in the dataset are:

| Rank | State | Total Sales |
|---:|---|---:|
| 1 | California | $457,687.63 |
| 2 | New York | $310,876.27 |
| 3 | Texas | $170,188.05 |
| 4 | Washington | $138,641.27 |
| 5 | Pennsylvania | $116,511.91 |
| 6 | Florida | $89,473.71 |
| 7 | Illinois | $80,166.10 |
| 8 | Ohio | $78,258.14 |
| 9 | Michigan | $76,269.61 |
| 10 | Virginia | $70,636.72 |

California has the highest total sales, followed by New York and Texas.

### 3. Regional Performance

| Region | Total Sales | Total Profit |
|---|---:|---:|
| West | $725,457.82 | $108,418.45 |
| East | $678,781.24 | $91,522.78 |
| Central | $501,239.89 | $39,706.36 |
| South | $391,721.91 | $46,749.43 |

The West has the highest total sales and total profit among the four regions in this dataset. The Central region has lower total profit than the other regions, despite generating more sales than the South.

### 4. Interactive Geographic Sales Map

The project includes an interactive choropleth map created with Folium and US state boundaries from a GeoJSON file.

The map provides:

- Geographic visualization of total sales by state.
- Color shading to compare sales levels.
- A legend showing total sales in USD.
- State names and total sales values in hover tooltips.
- Interactive zoom and map navigation.

The map is saved as `maps/sales_map.html`. Open this file in a web browser to explore the visualization.

### 5. Preliminary Expansion Screening

The expansion-screening script ranks states by historical sales and includes total profit, record counts, sales rank, and a profitability indicator.

These results can help identify markets for further investigation. However, the analysis does not establish whether a state or local area is underserved or whether opening another store would be commercially viable.

## Key Findings

- California leads the dataset in total sales, at approximately $457,688.
- New York ranks second, with approximately $310,876 in sales.
- The West region records the highest total sales and total profit.
- The Central region generates $501,239.89 in sales but only $39,706.36 in profit, making profitability worth investigating further.
- Historical sales and profit provide useful indicators of market performance, but they do not independently establish unmet demand or the best location for a new store.

## Limitations

- The dataset provides state and region labels rather than individual customer or store coordinates.
- The geographic map displays aggregated historical sales by state; it does not show sales at city, neighborhood, or individual-store level.
- The analysis does not include population, customer density, competitor locations, or existing store coverage.
- High sales do not necessarily indicate an underserved market or justify opening another store.
- The results describe the supplied dataset and should not be interpreted as a forecast of future performance.

## Recommended Next Steps

To strengthen the geographic analysis and support more reliable expansion decisions:

1. Add verified store locations and existing store coverage.
2. Obtain independent demand indicators, such as population, customer density, and local market size.
3. Consider competitor locations and accessibility when evaluating potential sites.
4. Analyze sales and profitability at a more detailed geographic level when suitable data becomes available.
5. Combine sales performance, local demand, competition, and store coverage to evaluate potential expansion locations.

## Outputs

The project generates the following files:

- `data/processed/sales_by_state.csv`
- `data/processed/sales_by_region.csv`
- `data/processed/state_sales_for_mapping.csv`
- `data/processed/preliminary_expansion_screening.csv`
- `screenshots/top_10_states_sales.png`
- `screenshots/sales_by_region.png`
- `screenshots/profit_by_region.png`
- `maps/sales_map.html`

## Conclusion

This project demonstrates a Python-based workflow for retail sales analysis, geographic visualization, and preliminary expansion screening. It combines state- and region-level analysis with an interactive choropleth map to make geographic sales patterns easier to explore.

The findings identify strong-performing markets and areas for further investigation. Additional store-location and local-demand data would be necessary to make evidence-based recommendations about where new stores should be opened.
