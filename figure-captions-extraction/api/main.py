
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
