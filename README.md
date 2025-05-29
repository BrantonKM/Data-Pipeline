# Data-Pipeline
# 📁 Project Structure (summary)
#
# - run_pipeline.py           -> Executes ETL pipeline
# - run_flask.py              -> Launches the Flask dashboard
# - config.py                 -> Stores database configuration
# - /scripts/
#     - extract.py           -> Extracts data from CSV
#     - transform.py         -> Transforms data into long format
#     - load.py              -> Loads data into PostgreSQL
# - /app/
#     - __init__.py          -> Flask app factory
#     - routes.py            -> Dashboard views
#     - templates/
#         - dashboard.html   -> Frontend UI
# - airtravel.csv            -> Source dataset