# config/logger_config.py

import logging
import os

# Ensure logs folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Logger configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("DataPipeline")