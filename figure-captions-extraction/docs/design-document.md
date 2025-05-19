
# Design Document

## 🔍 Overview

This system extracts structured metadata from scientific papers in **PubMed Central (PMC)**, focusing on:

- Title
- Abstract
- Figure captions
- Figure image URLs (if any)
- Named entities (e.g., genes) from captions using **BERN2**

It supports both batch processing (via CLI or files) and API-based access, and is deployed using **Docker** for portability.

---

## 🎯 Purpose

To design and implement a production-ready, extensible system that:

- Ingests a list of PMCIDs (optionally PMIDs in future).
- Extracts metadata including title, abstract, and all figure captions from scientific papers.
- Identifies biomedical named entities (e.g., genes, diseases) from figure captions using **BERN2**.
- Stores this data in a configurable backend (default: **DuckDB**).
- Makes data accessible through a secure **API** and **CLI**.

---

## 🧱 High-Level Architecture

```text
[CLI / API]
     │
     ▼
[Input Handler]    ── Reads PMCID list (file or API payload)
     │
     ▼
[PMC Fetcher]      ── Uses BioC PMC API to get article structure & figure captions
     │
     ▼
[Entity Extractor] ── Uses local BERN2 model to extract biomedical entities from captions
     │
     ▼
[Data Formatter]   ── Converts extracted data to JSON and/or CSV
     │
     ▼
[Storage Engine]   ── Stores structured data (default: DuckDB)
     │
     ▼
[REST API Server]  ── Serves queried data, password/API key protected
````

---

## 🧩 Key Components

| Component                 | Description                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| **CLI Runner**            | Accepts PMCID list as input file, runs extraction, saves output           |
| **PMC Fetcher**           | Queries BioC PMC API for title, abstract, and figure captions             |
| **BERN2 Extractor**       | Uses a local BERN2 server or subprocess to extract biomedical entities    |
| **Storage Backend**       | Saves data to DuckDB (modular for future DBs like PostgreSQL)             |
| **REST API (FastAPI)**    | Offers endpoints to upload IDs, fetch filtered data, and download results |
| **Dockerized Deployment** | Fully containerized environment, including optional DNS override          |

---

## 🏗️ System Layers

### 1. Input Layer

* Accepts list of PMCIDs via:

  * Command-line: `--ids ids.txt`
  * API upload (to be implemented)

### 2. Extraction Layer

* Uses **BioC-PMC API** to retrieve structured XML
* Extracts:

  * Paper title
  * Abstract
  * Figure captions
  * Figure URLs

### 3. Entity Recognition Layer

* Uses **BERN2** (local instance) for biomedical named entity recognition
* No external PubTator dependency

### 4. Storage Layer

* Saves metadata to:

  * DuckDB (default)
  * JSON or CSV (optional for inspection)

### 5. API Layer

* Built with **FastAPI**
* Enables:

  * Submission of new IDs
  * Filtered queries
  * Secure downloads (CSV, JSON)
  * Access control via password or API key

### 6. Configuration

* Managed via CLI flags or environment variables:

  * `--file`, `--format`
  * DB backend
  * Log level
  * Entity extractor (default: BERN2)

---

## 🖥️ Deployment Diagram

```text
┌──────────────────────────────┐
│     Client (User/Admin)      │
└────────────┬─────────────────┘
             │ REST/CLI
             ▼
     ┌───────────────┐
     │   Ingestion   │
     └───────────────┘
             │
             ▼
     ┌────────────────┐
     │  PMC API Fetch │ <─ External BioC API
     └────────────────┘
             │
             ▼
     ┌──────────────────┐
     │  BERN2 NER Model │ <─ Local Script or Server
     └──────────────────┘
             │
             ▼
     ┌────────────────┐
     │  DuckDB Engine │
     └────────────────┘
             │
             ▼
     ┌────────────────────┐
     │  FastAPI Server    │
     └────────────────────┘
```

---

## 🧰 Commands

* **Build image**

  ```bash
  docker build -t pubmed-parser .
  ```

* **Run batch job**

  ```bash
  docker run --rm -v $(pwd):/app pubmed-parser
  ```

* **Optional DNS override for PubMed API**

  ```bash
  docker run --rm --dns=8.8.8.8 -v $(pwd):/app pubmed-parser
  ```

---

## 📦 Dependencies and Justifications

| Dependency  | Purpose                             |
| ----------- | ----------------------------------- |
| Python 3.11 | Modern features, async support      |
| DuckDB      | Lightweight, embedded analytical DB |
| Requests    | External API calls                  |
| BERN2       | Local biomedical NER                |
| FastAPI     | High-performance web API            |
| Docker      | Reproducible deployment             |
| JSON / CSV  | Flexible output formats             |

---

## 🔐 Security

* API key/password protection via environment variables or `.env` file
* Docker sandboxing for the runtime
* Logs include timestamped entries for traceability

---

## 🌱 Future-Proofing & Extensibility

* **PMC to PMID** mapping via NCBI eutils planned
* Modular fetcher for adding new sources (e.g., arXiv)
* Pluggable storage backends (PostgreSQL, S3, etc.)
* Configurable logging, format, and authentication options


