
# Operationalization

This document provides a runbook for deploying, configuring, and operating the Figure Caption Extraction system. It includes setup instructions, Docker-based deployment, example configuration, and usage scenarios.

---

## 🚀 Deployment Overview

The system is built for reproducibility and portability using Docker and Python 3. It supports:

- Batch caption + entity extraction via CLI
- REST API for upload, query, and download
- Configurable storage backend (default: DuckDB)
- Remote BERN2 integration for biomedical named entity recognition

---

## 🐳 Docker-Based Deployment

### 1. Build the Docker Image

```bash
docker build -t pubmed-parser .
````

### 2. Run API Server

```bash
docker run -p 8000:8000 -v $(pwd):/app pubmed-parser uvicorn main:app --host 0.0.0.0 --port 8000
```

### 3. Run Batch CLI Job

```bash
docker run --rm -v $(pwd):/app pubmed-parser python cli/runner.py --ids input.txt --format csv
```

> ✅ Tip: If you're behind a firewall or need stable DNS resolution, you can override DNS:

```bash
docker run --dns=8.8.8.8 -v $(pwd):/app pubmed-parser ...
```

---

## ⚙️ Configuration

Configuration is managed via `config.py`.

### Example: `config.py`

```python
# config.py

API_KEY = "secure-api-key"
LOG_LEVEL = "INFO"  # or DEBUG

# Storage
DB_PATH = "data/figures.db"
OUTPUT_FORMAT = "csv"  # or json

# Remote BERN2 API
BERN2_URL = "http://bern2.korea.ac.kr/pubmed"

# PMC Source
PMC_API_BASE = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi"
```

> ✅ You can override this using environment variables inside `Dockerfile` or during runtime if needed.

---

## 📌 Sample Usage Scenarios

### ▶️ 1. Batch Extraction (CLI)

```bash
python cli/runner.py --ids input.txt --format csv
```

Where `input.txt` contains:

```
PMC1234567
PMC9876543
```

### ▶️ 2. Start API Server (Local Dev)

```bash
uvicorn main:app --reload
```

### ▶️ 3. Upload PMCIDs via API

```bash
curl -X POST http://localhost:8000/upload_pmcs \
  -H "x-api-key: your-secure-api-key" \
  -H "Content-Type: application/json" \
  -d '{"pmcids": ["PMC1234567", "PMC2345678"]}'
```

### ▶️ 4. Query Stored Captions

```bash
curl http://localhost:8000/query \
  -H "x-api-key: your-secure-api-key"
```

### ▶️ 5. Download CSV

```bash
curl http://localhost:8000/download?format=csv \
  -H "x-api-key: your-secure-api-key" -o output.csv
```

---

## 📓 Maintenance Notes

* **Database Reset**: To clear DuckDB for fresh runs, delete `data/figures.db`
* **Logs**: Logged to console with timestamp and level (INFO, DEBUG)
* **Security**: API key enforced on all endpoints; rotate keys periodically
* **Troubleshooting**:

  * BERN2 unreachable? Ensure remote URL is up: `http://bern2.korea.ac.kr`
  * PMC fetch failures? Check PMCID validity or API quota

---

## ✅ Checklist for Deployment

| Item                           | Status |
| ------------------------------ | ------ |
| Dockerfile complete            | ✅      |
| Volume mounted for persistence | ✅      |
| FastAPI running on port 8000   | ✅      |
| Remote BERN2 reachable         | ✅      |
| `config.py` populated          | ✅      |
| API key enforced               | ✅      |

