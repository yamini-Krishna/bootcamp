
'''
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse, JSONResponse
from typing import List
from pmc_api_client import PMCAPIClient
from pmc_parser import PMCParser
from csv_exporter import CSVExporter
from config import EXPORT_FOLDER  # Ensure EXPORT_FOLDER is defined in config.py
from json_exporter import JSONExporter
from data_sources.factory import get_data_source
from api.auth import get_api_key  # Ensure get_api_key is properly defined in api/auth.py
from storage.duckdb_backend import DuckDBStorage  # Ensure DuckDBStorage is properly implemented
import os
import json

# Initialize the FastAPI app
app = FastAPI()

# Initialize client, parser, and storage
client = PMCAPIClient()
parser_ = PMCParser()
storage = DuckDBStorage()

# Uncomment and use a Pydantic model for input validation
from pydantic import BaseModel
class PMCIDsRequest(BaseModel):
     pmcids: List[str]

# API endpoint to upload PMC IDs and fetch data
@app.post("/upload")
async def upload_ids(pmcids: List[str], api_key: str = Depends(get_api_key)):
    results = []
    source = get_data_source()  # Assuming this function returns a valid source to fetch PMC data
    for pmcid in pmcids:
        try:
            # Fetch XML data for the given PMC ID (uncomment if necessary)
            # xml = client.fetch_pmc_article(pmcid)
            xml = source.fetch(pmcid)
            if not xml:
                continue  # If no data is fetched, skip the PMC ID
            
            # Parse the fetched XML data
            parsed = parser_.parse(xml, pmcid)
            parsed["pmcid"] = pmcid  # Ensure the PMC ID is part of the parsed data
            
            # Append parsed data to results
            results.append(parsed)
            storage.save(parsed)  # Save to DuckDB (or any storage system you're using)
        except Exception as e:
            print(f"Error processing PMC ID {pmcid}: {e}")
            continue

    return {"processed": len(results), "failed": len(pmcids) - len(results)}

# API endpoint to fetch the results
@app.get("/results")
async def get_results(api_key: str = Depends(get_api_key)):
    data = storage.query_all()  # Query all records from the storage
    if not data:
        raise HTTPException(status_code=404, detail="No data found")

    columns = ["pmcid", "title", "journal", "abstract", "authors"]
    json_data = [dict(zip(columns, row)) for row in data]
    return JSONResponse(content=json_data)

# API endpoint to download data as CSV
@app.get("/download.csv")
async def download_csv(api_key: str = Depends(get_api_key)):
    data = storage.query_all()  # Query all records from the storage
    if not data:
        raise HTTPException(status_code=404, detail="No data to export")

    columns = ["pmcid", "title", "journal", "abstract", "authors"]
    records = [dict(zip(columns, row)) for row in data]

    # Initialize CSVExporter
    exporter = CSVExporter()
    os.makedirs(EXPORT_FOLDER, exist_ok=True)
    output_path = os.path.join(EXPORT_FOLDER, "export.csv")

    # If file exists, remove it before exporting
    if os.path.exists(output_path):
        os.remove(output_path)

    # Export records to CSV
    exporter.save_to_csv(records, output_path)
    return FileResponse(output_path, media_type="text/csv", filename="export.csv")

# API endpoint to download data as JSON
@app.get("/download.json")
async def download_json(api_key: str = Depends(get_api_key)):
    data = storage.query_all()  # Query all records from the storage
    if not data:
        raise HTTPException(status_code=404, detail="No data to export")

    columns = ["pmcid", "title", "journal", "abstract", "authors"]
    records = [dict(zip(columns, row)) for row in data]

    os.makedirs(EXPORT_FOLDER, exist_ok=True)
    output_path = os.path.join(EXPORT_FOLDER, "export.json")

    # If file exists, remove it before exporting
    if os.path.exists(output_path):
        os.remove(output_path)

    # Export records to JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=4)

    return FileResponse(output_path, media_type="application/json", filename="export.json")
'''
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse, JSONResponse
from typing import List
from pmc_api_client import PMCAPIClient
from pmc_parser import PMCParser
from csv_exporter import CSVExporter
from config import EXPORT_FOLDER
from json_exporter import JSONExporter
from data_sources.factory import get_data_source
from api.auth import get_api_key
from storage.duckdb_backend import DuckDBStorage
import os
import json

app = FastAPI()
client = PMCAPIClient()
parser = PMCParser()
storage = DuckDBStorage()


@app.post("/upload")
async def upload_ids(pmcids: List[str], api_key: str = Depends(get_api_key)):
    results = []
    source = get_data_source()
    for pmcid in pmcids:
        xml = source.fetch(pmcid)
        if not xml:
            continue
        parsed = parser.parse(xml, pmcid)
        parsed["pmcid"] = pmcid 
        results.append(parsed)
        storage.save(parsed)
    return {"processed": len(results), "failed": len(pmcids) - len(results)}


@app.get("/results")
async def get_results(api_key: str = Depends(get_api_key)):
    data = storage.query_all()
    columns = [
        "pmcid", "title", "abstract", 
        "figure_label", "figure_caption", 
        "figure_image_url", "figure_key_entities"
    ]
    json_data = [dict(zip(columns, row)) for row in data]
    return JSONResponse(content=json_data)


@app.get("/download.csv")
async def download_csv(api_key: str = Depends(get_api_key)):
    data = storage.query_all()
    if not data:
        raise HTTPException(status_code=404, detail="No data to export")

    columns = [
        "PMCID", "title", "abstract", 
        "figure_label", "figure_caption", 
        "figure_image_url", "figure_key_entities"
    ]
    records = [dict(zip(columns, row)) for row in data]

    os.makedirs(EXPORT_FOLDER, exist_ok=True)
    output_path = os.path.join(EXPORT_FOLDER, "export.csv")
    if os.path.exists(output_path):
        os.remove(output_path)

    exporter = CSVExporter()
    exporter.save_to_csv_api(records, output_path)
    return FileResponse(output_path, media_type="text/csv", filename="export.csv")


@app.get("/download.json")
async def download_json(api_key: str = Depends(get_api_key)):
    data = storage.query_all()
    if not data:
        raise HTTPException(status_code=404, detail="No data to export")

    columns = [
        "PMCID", "title", "abstract", 
        "figure_label", "figure_caption", 
        "figure_image_url", "figure_key_entities"
    ]
    records = [dict(zip(columns, row)) for row in data]

    os.makedirs(EXPORT_FOLDER, exist_ok=True)
    output_path = os.path.join(EXPORT_FOLDER, "export.json")
    if os.path.exists(output_path):
        os.remove(output_path)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=4)

    return FileResponse(output_path, media_type="application/json", filename="export.json")
