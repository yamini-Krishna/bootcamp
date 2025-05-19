
# CLI Usage

The CLI interface allows for batch ingestion and processing of PMCIDs using a local terminal. The CLI is useful for automation, scheduled jobs, and large-scale extraction workflows.

---

## 📦 Command Format

```bash
python cli/runner.py --ids input.txt --format csv
````

---

## 🔤 Arguments

| Argument    | Description                                 | Example             |
| ----------- | ------------------------------------------- | ------------------- |
| `--ids`     | Path to file containing PMCIDs              | `--ids pmc.txt`     |
| `--format`  | Output format: `csv` or `json`              | `--format csv`      |
| `--output`  | (Optional) Output filename                  | `--output data.csv` |
| `--dry-run` | (Optional) Preview captions only, no BERN2  | `--dry-run`         |
| `--limit`   | (Optional) Limit number of PMCIDs processed | `--limit 10`        |

---

## 📁 Input Format

A plain text file (`.txt`) with one PMCID per line:

```
PMC1234567
PMC7654321
PMC1122334
```


## 🧪 Example Usage

### Basic Usage

```bash
python cli/runner.py --ids pmcids.txt --format csv
```

### Dry Run (captions only, skip BERN2)

```bash
python cli/runner.py --ids pmcids.txt --format json --dry-run
```

### Limited Batch

```bash
python cli/runner.py --ids pmcids.txt --format csv --limit 5
```

---

## 🔧 Configuration

CLI uses values from `config.py`:

```python
API_KEY = "your-secure-api-key"
BERN2_URL = "http://bern2.korea.ac.kr/pubmed"
DB_PATH = "data/figures.db"
```

---

## 🛠️ Development Tip

Run in Docker (volume-mounted):

```bash
docker run --rm -v $(pwd):/app pubmed-parser \
  python cli/runner.py --ids pmcids.txt --format json
```

---

## ✅ Exit Codes

| Code | Meaning         |
| ---- | --------------- |
| 0    | Success         |
| 1    | Invalid input   |
| 2    | BERN2 failure   |
| 3    | Storage failure |

