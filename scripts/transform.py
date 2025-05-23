# scripts/transform.py

import pandas as pd
from config.logger_config import logger

def clean_data(csv_path: str) -> pd.DataFrame:
    logger.info(f"Cleaning data from {csv_path}...")
    try:
        df = pd.read_csv(csv_path)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        logger.info("✅ Data cleaned successfully.")
        return df
    except Exception as e:
        logger.error(f"❌ Failed to clean data: {e}")
        raise