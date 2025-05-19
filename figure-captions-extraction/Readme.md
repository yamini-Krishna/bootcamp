
# PubMed Figure Caption Extractor (FCE)

This tool fetches articles from PubMed Central (PMC) by PMCID, extracts figure captions and related metadata, annotates biomedical entities, and exports the data to CSV/JSON. It supports both CLI and REST API usage.

---

## 📁 Project Structure

```
.
├── api/
│   ├── __init__.py
│   ├── auth.py
│   └── main.py
│
├── config.py
├── csv_exporter.py
├── data/
│   ├── articles.duckdb
│   └── articles.duckdb.wal
│
├── data_sources/
│   ├── base.py
│   ├── factory.py
│   └── pmc_source.py
│
├── docker-compose.yaml
├── Dockerfile
├── exports/
│   ├── exports.csv
│   └── exports.json
│
├── ids.txt
├── json_exporter.py
├── logger_config.py
├── Makefile
├── pmc_api_client.py
├── pmc_parser.py
├── requirements.txt
├── run.py
└── storage/
    ├── __init__.py
    ├── base.py
    └── duckdb_backend.py
```
---

### 📦 Project File Overview

| File/Folder           | Purpose                                                                   |
| --------------------- | ------------------------------------------------------------------------- |
| `api/`                | FastAPI backend containing routes (`main.py`) and auth logic (`auth.py`). |
| `config.py`           | Global configuration settings (e.g. logging level, export folder).        |
| `csv_exporter.py`     | Exports parsed results to CSV from CLI or API.                            |
| `data/`               | Contains `articles.duckdb` storage with parsed article data.              |
| `data_sources/`       | Abstract + PMC-specific data source logic for fetching article XML.       |
| `docker-compose.yaml` | Defines container setup (optional use with Docker Compose).               |
| `Dockerfile`          | Docker setup for building and running the project image.                  |
| `exports/`            | Stores generated CSV and JSON export files.                               |
| `ids.txt`             | Text file listing PMCIDs to be parsed.                                    |
| `json_exporter.py`    | Exports parsed results to JSON from CLI.                                  |
| `logger_config.py`    | Logging configuration utility.                                            |
| `Makefile`            | Handy command shortcuts for build/run/test (optional).                    |
| `pmc_api_client.py`   | Handles fetching articles from PMC API.                                   |
| `pmc_parser.py`       | Parses XML to extract captions, figures, and metadata.                    |
| `requirements.txt`    | Python dependencies for installing the project.                           |
| `run.py`              | CLI entry point for fetching, parsing, and exporting.                     |
| `storage/`            | Storage backends; currently uses DuckDB for article storage.              |


---

## 🚀 Getting Started

### 1. 🔧 Build Docker Image

```bash
docker build -t pubmed-parser .
```

### 2. ▶️ Run the Container

Mount current directory for access to local files:

```bash
docker run --rm -v $(pwd):/app pubmed-parser
```

---

## 🐍 CLI Usage

### Debug mode (no export, just logging)

```bash
python run.py --ids ids.txt -d
```

### Export data to CSV

```bash
python run.py --ids ids.txt --format csv --file outputfce.csv
```
-outputfce.csv is present in the directory

### Export data to JSON

```bash
python run.py --ids ids.txt --format json --file outputfce.json
```
-outputfce.json is present in the directory

---

## 🌐 API Usage

Make sure the API is running. You can start it using:

```bash
uvicorn api.main:app --reload
```

> Default API Key: `aganitha123`

---

### 🔼 Upload PMCIDs for Processing

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Authorization: aganitha123" \
  -H "Content-Type: application/json" \
  -d "[\"PMC7074893\", \"PMC1234567\"]"
```

### 📥 Get All Parsed Results (JSON)

```bash
curl -X GET "http://localhost:8000/results" \
  -H "Authorization: aganitha123"
```

### 📄 Download as CSV

```bash
curl -L -H "Authorization: aganitha123" \
  "http://localhost:8000/download.csv" -o export.csv
```

### 📦 Download as JSON

```bash
curl -L -H "Authorization: aganitha123" \
  "http://localhost:8000/download.json" -o export.json
```

---

## 🛢️ Querying DuckDB Directly

```sql
-- Run this in DuckDB
.open data/articles.duckdb
SELECT * FROM articles;
```

---

## 🎥 Asciinema Recordings

Watch demos to understand how to use the project via CLI and API:

### CLI Usage and Docker

[![asciicast](https://asciinema.org/a/Tmj6NyuuEqlQIC5DxFccUoKkx.svg)](https://asciinema.org/a/Tmj6NyuuEqlQIC5DxFccUoKkx)

### API Server Running

[![asciicast](https://asciinema.org/a/yGzIpSMdpRZvirzcnoZGJax7T.svg)](https://asciinema.org/a/yGzIpSMdpRZvirzcnoZGJax7T)

### API Usage (Upload + Download)

[![asciicast](https://asciinema.org/a/Uszpa0X1C54yzkz7muajj1kKU.svg)](https://asciinema.org/a/Uszpa0X1C54yzkz7muajj1kKU)

---

## Features

* Fetch PMC XML articles
* Extract captions, labels, and figure images
* Entity extraction using BERN2 API
* Export to CSV/JSON
* Query results from DuckDB
* FastAPI-based REST endpoints
* Docker support

---

## 📝 Notes

* Data is saved in `data/articles.duckdb`
* Exports are saved in `exports/` folder
* Make sure the `EXPORT_FOLDER` in `config.py` points to `exports/`



