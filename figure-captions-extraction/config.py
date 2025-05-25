# config.py
import os

STORAGE_BACKEND = "duckdb"
API_KEY = os.getenv("API_KEY", "aganitha123") 
API_KEY_NAME = "Authorization"
DATA_SOURCE = "PMC"
LOG_LEVEL = "DEBUG"  # or "INFO", "ERROR", etc.
ENABLE_ENTITY_EXTRACTION = True


EXPORT_FOLDER = os.path.join(os.getcwd(), "exports")
os.makedirs(EXPORT_FOLDER, exist_ok=True)


