# ⚡ SQLite Setup, Testing & Bulk Insert Automation

This repository demonstrates how to effectively set up and test **SQLite**, a lightweight relational database engine, and how to automate and benchmark bulk data insertion — an essential skill in backend and data-oriented development workflows.

---

## 🚀 Objective

* Install and validate SQLite locally
* Create and manipulate an SQLite database (`example.db`)
* Automate the generation of 500+ SQL insert commands using Python (`generate_inserts.py`)
* Execute the commands via CLI using `insert_commands.sql`
* Benchmark the performance and understand how bulk transactions behave

---

## 🛠️ Setup Instructions

### ✅ Step 1: Install SQLite

**Linux:**

```bash
sudo apt update
sudo apt install sqlite3
```

**Windows/Mac:**

* Download from: [https://sqlite.org/download.html](https://sqlite.org/download.html)
* Optionally, install **DB Browser for SQLite** or VS Code SQLite plugins for UI access

---

### ✅ Step 2: Test Your Installation

1. Open terminal and type:

   ```bash
   sqlite3 example.db
   ```

2. Inside the prompt:

   ```sql
   CREATE TABLE COMPANIES (company_name VARCHAR(20), id INT);
   INSERT INTO COMPANIES VALUES ("aganitha", 1);
   .exit
   ```

3. Verify file type:

   ```bash
   file example.db  # Should say: SQLite 3.x database
   ```

---

## 📁 Project Files

| File                  | Description                                      |
| --------------------- | ------------------------------------------------ |
| `example.db`          | SQLite database created and used in exercises    |
| `generate_inserts.py` | Python script to generate 500 insert statements  |
| `insert_commands.sql` | Output SQL file with generated INSERT statements |

---

## 🧪 Bulk Insert Exercise

### 🔧 Step 1: Generate 500 Inserts

Run the Python script:

```bash
python generate_inserts.py
```

This creates `insert_commands.sql` with 500 INSERT statements for the `COMPANIES` table.

### ⚡ Step 2: Execute Inserts via SQLite CLI

```bash
time sqlite3 example.db < insert_commands.sql
```

You’ll see timing output like:

```bash
real    0m0.032s
user    0m0.005s
sys     0m0.002s
```

---

## 💡 Optimization Tip

For faster execution, wrap inserts in a transaction block in `insert_commands.sql`:

```sql
BEGIN TRANSACTION;
-- INSERT statements here
COMMIT;
```

This significantly reduces disk I/O overhead and boosts performance (up to 10x faster).

---

## 📊 Why This Matters

* Demonstrates real-world performance considerations
* Reinforces importance of transaction handling
* Builds automation skills for database scripts
* Useful for seeding dev/test environments or load testing



