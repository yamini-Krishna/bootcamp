
# Figure Caption Extraction and Access System

Welcome to the official documentation for the Figure Caption Extraction and Access System.

---

## 🎯 Project Purpose

This system extracts, stores, and serves key metadata from scientific publications, including:

- Title
- Abstract
- Figure captions (list)
- URLs for figures (if any)
- Key entities (e.g., genes) mentioned in figure captions

The initial focus is on PubMed Central (PMC) articles, but the architecture supports future expansion to other sources.

---

## 🚀 User Roles & Expectations

### As a User
- Submit paper IDs (PMC or PMID) for extraction
- Query extracted data via API (JSON/CSV)
- Upload lists via API or CLI

### As an Admin
- Configure storage backend (default: DuckDB)
- Set API authentication (password or API key)
- Choose data sources (extendable)
- Manage logging levels

### As an Operations Person
- Deploy via Docker
- Run batch ingestion jobs (file input, uploads, watched folders)
- Monitor logs and job statuses
- Ensure clean startup and shutdown of the system

---

## 📚 Documentation Sections

- [Design Document](design-document.md) — Architecture and key components
- [Implementation](implementation.md) — Codebase overview
- [Testing Plan](testing.md) — Functional, security, and performance testing
- [Operationalization](operationalization.md) — Deployment instructions and runbook
- [API Reference](api.md) — Endpoints and usage examples
- [CLI Usage](cli.md) — Command-line tools and options

---

## 🔗 Useful Links

- Source code repository: [GitHub link](https://github.com/yamini-Krishna/bootcamp/tree/main/figure-captions-extraction)
- Demo API endpoint: [http://localhost:8000](http://localhost:8000) (when running locally)

---

## 📞 Contact

For questions or support, reach out at yaminimusku04@example.com

