# storage/__init__.py

from config import STORAGE_BACKEND

def get_storage_backend():
    if STORAGE_BACKEND == "duckdb":
        from .duckdb_backend import DuckDBStorage
        return DuckDBStorage()
    else:
        raise NotImplementedError(f"Storage backend '{STORAGE_BACKEND}' is not supported.")
