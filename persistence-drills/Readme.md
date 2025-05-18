# Persistence-drills

#### 🗂️ **Folder 1: Persistence using File and DB**

* ✅ **Pickle Serialization/Deserialization:**

  * Created `Person` class and serialized/deserialized using `pickle`.
* ✅ **JSON Handling:**

  * Implemented `Book` class with `to_json()` and `from_json()`.
* ✅ **YAML Handling:**

  * Used `PyYAML` to serialize/deserialize `Car` class.
* ✅ **Advanced Serialization:**

  * Implemented custom `Graph` serialization (nodes, edges).
  * Skipped sensitive data in `User` class.
  * Implemented game state save/load.
  * Handled versioning changes in a class.
  * Serialized a `MyCollection` class.
  * Handled cyclic references using custom hooks.

---

#### 🗂️ **Folder 2: SQLite Basics**

* ✅ Reviewed:

  * Transactions and ACID properties.
  * File system reliability comparison.
  * Use cases where ACID properties can be relaxed.

---

#### 🗂️ **Folder 3: System Preparation**

* ✅ Installed and tested SQLite:

  * Created and populated `COMPANIES` table.
  * Exported and moved DB file across systems.
* ✅ Insert Generator:

  * Wrote and timed a program to generate 500 SQL inserts.

---

#### 🗂️ **Folder 4: Using SQLite3 with Python**

* ✅ Setup `store.db` and `products` table.
* ✅ Implemented and tested:

  * Insertion, fetching, updating, and deleting records.
  * Created a `Product` class encapsulating DB logic.
  * Added exception handling and validation.
  * Implemented transactions for data integrity.
  * Added `categories` table and join queries.
  * Aggregated product value.
  * Exported table data to CSV.
  * Batch insert with transaction support.
  * Banking transaction simulation (debit/credit in one transaction).
  * Inventory logic with transactional integrity.

---

#### 🗂️ **Folder 5: Advanced Python - ORM with SQLAlchemy + Pydantic**

* ✅ Practiced:

  * Defined SQLAlchemy models and Pydantic schemas.
  * CRUD operations with validation.
  * Filters, updates, deletes.
  * User-Post relationship setup and fetch.
  * Bulk inserts with rollback on error.
  * Converted code to async using SQLAlchemy 2.0.

---

#### 🗂️ **Folder 6: Real-World System Drills**

### ✅ Goals:

* Make informed **design decisions** like a professional backend engineer.
* Handle **schema evolution**, **data integrity**, **transactional safety**, and **real-life edge cases**.
* Practice **trade-off analysis** and **system recovery strategies**.


### 🚀 Drills Overview

#### 1. **Schema Evolution and Migrations**

* Start with a `users` table: `id`, `name`.
* Then simulate a schema change: add `created_at`.
* Practice: use **migrations**, **data backfilling**, and **version-aware code**.

#### 2. **Soft Deletes vs Hard Deletes**

* Implement both approaches.
* Discuss trade-offs: space vs accuracy, audit trails, performance.

#### 3. **Archiving Old Data**

* Move rows older than a threshold to an archive table.
* Implement archiving and querying logic.

#### 4. **Data Auditing**

* Track who made changes and when.
* Implement a basic auditing layer (e.g., trigger or app logic).

#### 5. **System Recovery Plan**

* Simulate failure: corrupted DB or power outage mid-transaction.
* Devise a recovery script: from backups, rollback logs, or checksums.

#### 6. **Rate-Limiting at Persistence Layer**

* Prevent abuse via DB-backed rate-limiting (e.g., `user_requests` table).
* Use timestamps to enforce limits (e.g., 100 requests/hour).

#### 7. **Caching Layer Integration**

* Add Redis/memory cache for a read-heavy API.
* Sync data and avoid stale reads.

#### 8. **Handling Write Conflicts**

* Simulate two writers updating same row.
* Implement conflict detection (e.g., optimistic locking using version field).

#### 9. **Idempotent Writes**

* Design APIs where repeated POST requests don’t cause duplicate inserts.
* Use unique constraints or idempotency tokens.

#### 10. **Multi-Tenant Design**

* Modify schema to support multiple tenants.
* Ensure data isolation and query efficiency.


