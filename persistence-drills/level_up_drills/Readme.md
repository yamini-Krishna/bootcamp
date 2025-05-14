

### 📘 Level Up Drills – Advanced SQLAlchemy & DB Techniques

Welcome to **Level Up Drills** – a collection of focused exercises designed to deepen your understanding of database modeling, SQLAlchemy, and real-world backend challenges. Each folder is a self-contained drill with Python code to demonstrate best practices.

---

### 📁 Directory Structure

```
level_up_drills/
├── 01_schema_migration/
├── 02_model_boundary_enforcement/
├── 03_idempotent_upserts/
├── 04_versioned_data_storage/
├── 05_concurrency_handling/
├── 06_large_binary_data/
├── 07_schema_vs_code_first/
├── 08_soft_deletes/
└── 09_large_dataset_testing/
```

---

### 🧩 Drill Descriptions

#### ✅ `01_schema_migration/`

* **Focus:** How to handle schema changes safely.
* **What it does:** Simulates adding/removing columns using migration tools (e.g., Alembic or raw SQL).
* **Why it matters:** Schema evolution is critical in production systems.

---

#### ✅ `02_model_boundary_enforcement/`

* **Focus:** Data validation at the model level.
* **What it does:** Enforces constraints like allowed types, string lengths, or required fields before DB writes.
* **Why it matters:** Prevents invalid data from reaching the database layer.

---

#### ✅ `03_idempotent_upserts/`

* **Focus:** Insert or update records without creating duplicates.
* **What it does:** Uses `ON CONFLICT` (PostgreSQL) or merge logic to safely upsert records.
* **Why it matters:** Ensures data consistency when processing repeated or retryable events.

---

#### ✅ `04_versioned_data_storage/`

* **Focus:** Storing history of changes to a record.
* **What it does:** Implements versioning using `version_id`, timestamps, or audit tables.
* **Why it matters:** Essential for traceability and regulatory compliance.

---

#### ✅ `05_concurrency_handling/`

* **Focus:** Avoiding race conditions and data corruption.
* **What it does:** Demonstrates row-level locking or optimistic concurrency using version counters.
* **Why it matters:** Ensures safe multi-user or multi-threaded access to shared resources.

---

#### ✅ `06_large_binary_data/`

* **Focus:** Handling images, files, or binary blobs in databases.
* **What it does:** Stores and retrieves large binary objects using BLOB columns or file references.
* **Why it matters:** Important for apps that manage files, photos, or documents.

---

#### ✅ `07_schema_vs_code_first/`

* **Focus:** Comparison between schema-first and code-first modeling.
* **What it does:** Shows how to define models based on existing schema (schema-first) vs generate schema from models (code-first).
* **Why it matters:** Helps decide approach based on team and project requirements.

---

#### ✅ `08_soft_deletes/`

* **Focus:** Non-destructive record deletion.
* **What it does:** Marks records as deleted by setting a `deleted_at` timestamp instead of removing them.
* **Why it matters:** Preserves data history while hiding deleted items from the UI.

---

#### ✅ `09_large_dataset_testing/`

* **Focus:** Testing and benchmarking with large data.
* **What it does:** Inserts 1 million+ records using naive and batch methods to compare performance.
* **Why it matters:** Useful for scalability, performance, and stress testing.

---

### 🛠 Requirements

Install SQLAlchemy and optionally SQLite for lightweight testing:

```bash
pip install sqlalchemy
```

---

### 🧪 How to Run

Each folder contains a standalone Python file. You can run each drill independently like so:

```bash
cd level_up_drills
python 07_schema_vs_code_first.py
```

Make sure the database (`.db` files) is writable and not locked by other processes during testing.

