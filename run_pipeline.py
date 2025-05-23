# run_pipeline.py

from scripts.extract import download_csv
from scripts.transform import clean_data
from scripts.load import load_to_postgres
from config.logger_config import logger

def main():
    logger.info("🚀 Starting Data Pipeline")

    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    csv_path = "data/airtravel.csv"
    table_name = "airtravel_data"

    try:
        downloaded = download_csv(url, csv_path)
        cleaned = clean_data(downloaded)
        load_to_postgres(cleaned, table_name)
        logger.info("✅ Pipeline finished successfully.")
    except Exception as e:
        logger.error(f"❌ Pipeline failed: {e}")

if __name__ == "__main__":
    main()
