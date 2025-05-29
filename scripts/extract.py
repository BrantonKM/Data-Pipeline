import pandas as pd
import logging
from config import DATA_FILE

def extract_data(file_path=DATA_FILE):
    try:
        df = pd.read_csv(file_path)
        logging.info("Data extracted successfully.")
        return df
    except Exception as e:
        logging.error(f"Failed to extract data: {e}")
        raise
