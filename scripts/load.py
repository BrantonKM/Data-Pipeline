# scripts/load.py

import psycopg2
from config.db_config import DB_CONFIG
from config.logger_config import logger

def load_to_postgres(df, table_name: str):
    logger.info(f"Loading data into table `{table_name}`...")
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        # Optional: drop and recreate table for dev/testing
        cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
        cursor.execute(f"""
            CREATE TABLE {table_name} (
                month TEXT,
                "1958" INT,
                "1959" INT,
                "1960" INT
            );
        """)
        for _, row in df.iterrows():
            cursor.execute(f"""
                INSERT INTO {table_name} (month, "1958", "1959", "1960")
                VALUES (%s, %s, %s, %s)
            """, tuple(row))
        conn.commit()
        logger.info("✅ Data loaded into PostgreSQL.")
    except Exception as e:
        logger.error(f"❌ Failed to load data: {e}")
    finally:
        cursor.close()
        conn.close()
