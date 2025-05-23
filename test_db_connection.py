# test_db_connection.py

import psycopg2
from config.db_config import DB_CONFIG

try:
    conn = psycopg2.connect(**DB_CONFIG)
    print("✅ Successfully connected to the database.")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
