# scripts/load.py


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from sqlalchemy import create_engine
from config.db_config import DB_CONFIG

def load_to_postgres(df, table_name):
    try:
        url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        engine = create_engine(url)
        
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"[✓] Data loaded to PostgreSQL table: {table_name}")
    except Exception as e:
        print(f"[✗] Error loading to database: {e}")

# Quick test
if __name__ == "__main__":
    from transform import clean_data
    df = clean_data("data/raw_data.csv")
    load_to_postgres(df, "airtravel_data")