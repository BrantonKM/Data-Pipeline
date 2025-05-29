import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data file path
DATA_FILE = os.path.join(BASE_DIR, "airtravel.csv")

# Log file path
LOG_FILE = os.path.join(BASE_DIR, "pipeline.log")

# For database configuration
DB_CONFIG = {
    "user": "postgres",
    "password": "Kalekye1222",
    "host": "localhost",
    "port": "5432",
    "database": "data_pipeline"
}
