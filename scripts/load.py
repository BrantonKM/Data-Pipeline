import pandas as pd
from sqlalchemy import create_engine
import logging
from config import DB_CONFIG

def load_data(df, table_name="airtravel_data"):
    try:
        db_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
                 f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info("Data loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise
