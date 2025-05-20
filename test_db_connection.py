# test_db_connection.py

import psycopg2
from config.db_config import DB_CONFIG

try:
    connection = psycopg2.connect(
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database']
    )
    print("✅ Successfully connected to the database.")
    connection.close()
except Exception as e:
    print(f"❌ Failed to connect to the database: {e}")
