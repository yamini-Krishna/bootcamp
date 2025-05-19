
# Testing Plan

This document outlines the phased implementation and testing approach for the Figure Caption Extraction and Access System.

---

## 🚧 Phased Implementation Plan

### Phase 1: Core Backend Infrastructure

**Goals:**
- Build a modular backend structure
- Set up DuckDB as the default storage backend
- Use `config.py` for all configuration (API keys, logging, etc.)

**Steps:**
1. Set up project folders:
    ```bash
    mkdir -p pmc bern2 storage api
    touch config.py main.py
    pip install fastapi uvicorn duckdb httpx
    ```

2. Define configuration in `config.py`:
    ```python
    API_KEY = "your_secure_api_key"
    STORAGE_BACKEND = "duckdb"
    LOG_LEVEL = "INFO"
    REMOTE_BERN2_URL = "http://bern2.korea.ac.kr/pubmed"
    ```

---

### Phase 2: API Layer Development

**Goals:**
- Build FastAPI endpoints:
  - Upload PMCIDs
  - Query stored caption/entity data
  - Download data (CSV or JSON)
- Secure endpoints using API key from `config.py`

**Run server:**
```bash
uvicorn main:app --reload
````

**Test endpoints:**

```bash
# Upload PMCIDs
curl -X POST http://localhost:8000/upload_pmcs -H "x-api-key: your_secure_api_key" -H "Content-Type: application/json" -d '{"pmcids": ["PMC1234567"]}'

# Query stored data
curl http://localhost:8000/query -H "x-api-key: your_secure_api_key"

# Download data
curl "http://localhost:8000/download?format=csv" -H "x-api-key: your_secure_api_key" -o results.csv
```

---

### Phase 3: BERN2 Integration (Remote)

**Goals:**

* Integrate with **remote BERN2 API** (no Docker needed)

**Verify remote BERN2:**

```bash
curl -X POST http://bern2.korea.ac.kr/pubmed -d "text=BRCA1 mutations cause breast cancer"
```

**Example usage in Python:**

```python
import httpx
resp = httpx.post("http://bern2.korea.ac.kr/pubmed", data={"text": "TP53 is mentioned in this figure."})
entities = resp.json()
```

---

### Phase 4: Data Export and Logging

**Goals:**

* Enable logging (based on level in `config.py`)
* Add download endpoints for JSON and CSV

**Example endpoints:**

```bash
curl http://localhost:8000/download?format=json -H "x-api-key: your_secure_api_key" -o data.json
curl http://localhost:8000/download?format=csv -H "x-api-key: your_secure_api_key" -o data.csv
```

---

### Phase 5: Extensibility and Plugin Support

**Goals:**

* Add abstract interfaces for:

  * Multiple data sources (PMC, future support for PMIDs)
  * Pluggable storage backends (PostgreSQL, etc.)
* Modular registration pattern

---

## ✅ Testing Plan

### 1. Functionality Testing

* Upload PMCIDs
* Run extraction
* Query and export results

```bash
curl -X POST http://localhost:8000/upload_pmcs -H "x-api-key: your_secure_api_key" -d '{"pmcids": ["PMC1234567"]}'
curl http://localhost:8000/query -H "x-api-key: your_secure_api_key"
```

---

### 2. Security Testing

* Ensure API key is required for all endpoints

```bash
# Without API key
curl http://localhost:8000/query
# → Expect: 401 Unauthorized

# With wrong key
curl http://localhost:8000/query -H "x-api-key: wrongkey"
# → Expect: 401 Unauthorized
```

---

### 3. Performance Testing

* Batch upload large PMCIDs
* Measure response and memory

```bash
curl -X POST http://localhost:8000/upload_pmcs -H "x-api-key: your_secure_api_key" -d '{"pmcids": ["PMC1", "PMC2", ..., "PMC100"]}'
top
htop
```

---

### 4. Mocked vs Real Data

* **Mocked:** Use sample XML to test parsing logic
* **Real:** Use real PMCIDs to validate end-to-end results

---

## 📌 Summary

* The system is implemented in phases with modularity in mind.
* It uses `config.py` for configuration and the **remote BERN2 API**.
* Security, performance, and functionality are tested at every stage.
* The system is easily extensible for new sources, formats, and backends.


