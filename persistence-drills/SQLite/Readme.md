# 🧠 Database Programming Primer — Practice & Principles

Welcome to the **Database Programming Primer**, a practical knowledge and drill series for developers who are comfortable with the basics and ready to move into real-world database application development.

This module **does not reteach SQL syntax** — instead, it sharpens your understanding of how databases behave under real usage, with a strong emphasis on **ACID properties**, **transactions**, and **design decisions**.

---

## 🧪 Knowledge Check — Key Concepts

### 🔄 What are Transactions?

A **transaction** is a sequence of one or more SQL operations treated as a **single unit of work**. Either **all operations succeed**, or **none do**. Transactions ensure data consistency in concurrent or failure-prone environments.

### 🧱 What is ACID?

| Property            | Description                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| **A** - Atomicity   | All operations in a transaction are treated as one. No partial execution. |
| **C** - Consistency | Database transitions from one valid state to another.                     |
| **I** - Isolation   | Transactions appear to run independently of each other.                   |
| **D** - Durability  | Committed changes survive system crashes.                                 |

---

## 🔍 Thought Questions (Reflect + Discuss)

1. **What if you don’t have transactions?**
   The system becomes error-prone. Imagine transferring money between accounts without ensuring both debit and credit happen atomically — leads to data corruption.

2. **What properties does your file system have?**
   Most file systems don’t support full ACID. They may support durability and partial atomicity (e.g., file renaming), but **no isolation or rollback**.

3. **What happens when a database lacks...**

| Missing             | Result                                                | When It's OK                                                            |
| ------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------- |
| **A - Atomicity**   | Partial changes can leave data in inconsistent state. | OK in analytics pipelines where failures are expected and recoverable.  |
| **C - Consistency** | Invalid data may persist.                             | OK in distributed systems temporarily using eventual consistency.       |
| **I - Isolation**   | Dirty reads, lost updates.                            | OK in read-heavy systems prioritizing performance (e.g., cache layers). |
| **D - Durability**  | Data may be lost after crash.                         | OK for non-critical data like logs or metrics in dev environments.      |

---

## 🧰 Choosing the Right Database

### 🔹 Key-Value Store: Use **Redis**

* Fast and simple (get/set)
* Great for caching, ephemeral data, feature flags

### 🔸 Relational Database: Use **SQLite or Postgres**

| Use Case                                        | Recommendation |
| ----------------------------------------------- | -------------- |
| Single-user apps, embedded systems              | `SQLite`       |
| Web apps where DB is accessed only via backend  | `SQLite`       |
| Multi-app access, concurrent reporting, scaling | `PostgreSQL`   |
| Transactions, ACID compliance                   | `PostgreSQL`   |

---

## 🛠 What's Included (Sample Practice Ideas)

* ✅ Implement simple transaction scenarios using SQLite and Postgres
* ✅ Simulate partial failure and recovery with/without ACID
* ✅ Log transaction state in file vs. database — compare outcomes
* ✅ Use Redis as a session or cache layer and observe non-durable data loss
* ✅ Benchmark: Compare latency for reads in Redis vs. Postgres

---

## ⚙️ Tools Recommended

* **SQLite CLI** or DB Browser for SQLite
* **PostgreSQL** with `psql` or `pgAdmin`
* **Redis** CLI for quick experiments
* **Python** or **Node.js** for code-based exercises

---

## 💡 Pro Tip: Treat Your Database Like a Codebase

* Use **schema migrations** (e.g., Alembic for Python, Flyway for Java)
* Keep **SQL queries versioned** in your repository
* Write **unit tests** for database logic (triggers, functions)

---

## ✅ Goal of This Module

By the end, you should:

* Understand when and **why to use transactions**
* Know the **implications of relaxing ACID guarantees**
* Choose the **right DB for your use case**
* Be ready to **implement fault-tolerant, data-consistent applications**

