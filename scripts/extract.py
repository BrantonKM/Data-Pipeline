# scripts/extract.py

import os
import requests
import pandas as pd
from config.logger_config import logger

def download_csv(url: str, download_path: str) -> str:
    logger.info("Starting download from URL...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(download_path, 'wb') as f:
            f.write(response.content)
        logger.info(f"✅ CSV downloaded to {download_path}")
        return download_path
    except Exception as e:
        logger.error(f"❌ Failed to download CSV: {e}")
        raise
