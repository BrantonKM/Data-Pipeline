# run_pipeline.py

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from scripts.extract import download_csv
from scripts.transform import clean_data
from scripts.load import load_to_postgres

DATA_URL = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
RAW_PATH = "data/raw_data.csv"
TABLE_NAME = "airtravel_data"

def run():
    print("\n🚀 Starting Data Pipeline...\n")

    # Step 1: Extract
    print("📥 Extracting data...")
    os.makedirs("data", exist_ok=True)
    download_csv(DATA_URL, RAW_PATH)

    # Step 2: Transform
    print("\n🧹 Transforming data...")
    clean_df = clean_data(RAW_PATH)
    if clean_df is None:
        print("⚠️ Transformation failed. Stopping pipeline.")
        return

    # Step 3: Load
    print("\n🛢️ Loading data into PostgreSQL...")
    load_to_postgres(clean_df, TABLE_NAME)

    print("\n✅ Pipeline completed successfully.\n")

if __name__ == "__main__":
    run()