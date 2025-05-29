import logging
from config import LOG_FILE
from scripts.extract import extract_data
from scripts.transform import transform_airtravel_data
from scripts.load import load_data

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

try:
    logging.info("🚀 Starting pipeline...")
    print("📥 Extracting data...")
    raw_df = extract_data()
    
    print("🔧 Transforming data...")
    clean_df = transform_airtravel_data(raw_df)
    print("✅ Transformed DataFrame preview:")
    print(clean_df.head())

    print("💾 Loading data...")
    load_data(clean_df, table_name="airtravel_data")
    logging.info("✅ Pipeline executed successfully.")
    print("✅ Pipeline executed successfully.")

except Exception as e:
    logging.error("❌ Pipeline execution failed.", exc_info=True)
    print(f"❌ Pipeline execution failed. Reason: {e}")
