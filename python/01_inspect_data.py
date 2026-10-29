
from pathlib import Path
import pandas as pd

# Locate the project and dataset folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "raw"

# Find CSV files in the raw data folder
csv_files = list(DATA_DIR.glob("*.csv"))

if not csv_files:
    print("No CSV file found!")
    print("Please place your sales dataset in:")
    print(DATA_DIR)
else:
    file_path = csv_files[0]
    print(f"Dataset found: {file_path.name}")

    # Load the dataset
    df = pd.read_csv(file_path)

    # Display basic information
    print("\nFirst five rows:")
    print(df.head())

    print("\nDataset dimensions:")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nMissing values per column:")
    print(df.isnull().sum())
