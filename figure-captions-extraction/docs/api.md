
# API Reference

This document outlines the available REST API endpoints for the Figure Caption Extraction System. All endpoints require an API key (`x-api-key`) as defined in `config.py`.

---

## 🔐 Authentication

Every request must include:

```http
x-api-key: your-secure-api-key
````

---

## 🚀 Endpoints

### 1. Upload PMCIDs

**POST** `/upload_pmcs`

Upload one or more PMCIDs for processing.

#### Request

```json
{
  "pmcids": ["PMC1234567", "PMC7654321"]
}
```

#### cURL Example

```bash
curl -X POST http://localhost:8000/upload_pmcs \
  -H "Content-Type: application/json" \
  -H "x-api-key: your-secure-api-key" \
  -d '{"pmcids": ["PMC1234567", "PMC7654321"]}'
```

#### Response

```json
{
  "status": "success",
  "processed": 2
}
```

---

### 2. Query Stored Captions

**GET** `/query`

Retrieve all stored figure captions and extracted entities.

#### cURL Example

```bash
curl http://localhost:8000/query \
  -H "x-api-key: your-secure-api-key"
```

#### Response

```json
[
  {
    "pmcid": "PMC1234567",
    "caption": "Figure shows BRCA1 mutation...",
    "entities": ["BRCA1"]
  },
  ...
]
```

---

### 3. Download Data

**GET** `/download?format=csv|json`

Download processed data in your preferred format.

#### CSV Example

```bash
curl http://localhost:8000/download?format=csv \
  -H "x-api-key: your-secure-api-key" \
  -o output.csv
```

#### JSON Example

```bash
curl http://localhost:8000/download?format=json \
  -H "x-api-key: your-secure-api-key" \
  -o output.json
```

#### Response (based on format)

* `csv`: File with columns like `pmcid,caption,entities`
* `json`: Array of JSON objects

---

## ❌ Error Responses

| Status Code | Message               | Reason                          |
| ----------- | --------------------- | ------------------------------- |
| 401         | Unauthorized          | Missing or invalid API key      |
| 400         | Bad Request           | Malformed JSON / missing fields |
| 500         | Internal Server Error | Any uncaught exception          |

---

## 🛡️ Security

* All endpoints require a valid API key.
* Define your key in `config.py` → `API_KEY = "your-secure-api-key"`

