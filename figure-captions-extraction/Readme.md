
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
python run.py --ids ids.txt --format csv --file output.csv
```

### Export data to JSON

```bash
python run.py --ids ids.txt --format json --file output.json
```

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

## ✅ Features

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



