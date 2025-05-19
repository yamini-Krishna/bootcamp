
# 🧬 PubMed Figure Caption Entity Extractor (FCE)

This project fetches articles from PubMed Central (PMC), parses figure captions, and extracts key biological entities using the BERN2 API. It supports both **CLI** and **FastAPI** usage, with export options in CSV and JSON.

---

## 📁 Project Structure

```
.
├── api/                      # FastAPI app (endpoints)
├── config.py                 # Configuration settings
├── csv_exporter.py           # CSV export logic
├── json_exporter.py          # JSON export logic
├── pmc_api_client.py         # Fetches article XML from PMC
├── pmc_parser.py             # Parses XML and figures
├── storage/                  # Storage backends (DuckDB)
├── data_sources/             # Data source factory and interfaces
├── run.py                    # CLI entry point
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker container definition
├── docker-compose.yaml       # Docker service runner
├── Makefile                  # Optional commands
├── ids.txt                   # Example PMCIDs list
```

---

## 🚀 Quick Start

### ✅ 1. Build Docker Image

```bash
docker build -t pubmed-parser .
```

### ▶️ 2. Run (Mount Current Directory)

```bash
docker run --rm -v $(pwd):/app pubmed-parser
```

---

## 🐍 CLI Usage

### 📄 Debug Mode (no file output)

```bash
python run.py --ids ids.txt -d
```

### 📤 Export as CSV

```bash
python run.py --ids ids.txt --format csv --file output.csv
```

### 📤 Export as JSON

```bash
python run.py --ids ids.txt --format json --file output.json
```

---

## 🌐 FastAPI Usage

### ⚙️ Start the API

```bash
uvicorn api.main:app --reload
```

---

## 🔐 Authentication

All API endpoints require an **API key** passed via the `Authorization` header.

**Default key:** `aganitha123` (from `config.py`)

---

### 📥 Upload PMCIDs for Processing

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Authorization: aganitha123" \
  -H "Content-Type: application/json" \
  -d "[\"PMC7074893\", \"PMC1234567\"]"
```

### 📄 View All Parsed Results

```bash
curl -X GET "http://localhost:8000/results" \
  -H "Authorization: aganitha123"
```

### 📥 Download CSV Export

```bash
curl -L -H "Authorization: aganitha123" \
  "http://localhost:8000/download.csv" -o export.csv
```

### 📥 Download JSON Export

```bash
curl -L -H "Authorization: aganitha123" \
  "http://localhost:8000/download.json" -o export.json
```

---

## 🛢️ DuckDB Storage

The parsed results are stored in:

```bash
data/articles.duckdb
```

To inspect:

```sql
-- Open in duckdb shell
duckdb data/articles.duckdb

-- Then run
SELECT * FROM articles;
```

---

## 📎 Example Files

* `ids.txt`: List of PMCIDs
* `output.csv`, `output.json`: CLI exports
* `export.csv`, `export.json`: API exports

---

## 🧪 Test Commands (Summary)

```bash
# CLI - Debug
python run.py --ids ids.txt -d

# CLI - CSV export
python run.py --ids ids.txt --format csv --file output.csv

# CLI - JSON export
python run.py --ids ids.txt --format json --file output.json

# API - Upload
curl -X POST "http://localhost:8000/upload" \
  -H "Authorization: aganitha123" \
  -H "Content-Type: application/json" \
  -d "[\"PMC7074893\", \"PMC1234567\"]"

# API - View
curl -X GET "http://localhost:8000/results" \
  -H "Authorization: aganitha123"

# API - CSV download
curl -L -H "Authorization: aganitha123" \
  "http://localhost:8000/download.csv" -o export.csv

# API - JSON download
curl -L -H "Authorization: aganitha123" \
  "http://localhost:8000/download.json" -o export.json
```

---

Let me know if you want badges, example outputs, screenshots, or to convert this to Markdown or PDF.
