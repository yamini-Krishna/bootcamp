# 🗃️ SQLite Practice with Python – Mini Projects Suite

Welcome to this curated set of practical exercises and mini projects to master SQLite with Python. This project will walk you through everything from basic CRUD operations to real-world transactional logic using Python’s built-in `sqlite3` module.

---

## 📦 Project Structure

```bash
.
├── example.db
├── generate_inserts.py
├── insert_commands.sql
├── database_output.png
├── store.db
├── requirements.txt
├── products_data.csv
├── Readme.md
├── 1_create_store_db.py
├── 2_create_products_table.py
├── 3_insert_product.py
├── 4_read_products.py
├── 5_update_product_price.py
├── 6_delete_product.py
├── 7_product_class.py
├── 8_product_with_exceptions.py
├── 9_search_product_by_name.py
├── 10_product_with_validation.py
├── 11_using_transactions.py
├── 12_join_queries
│   ├── 12_create_tables.py
│   ├── 12_insert_sample_data.py
│   └── 12_product_class.py
├── 13_aggregation_queries.py
├── 14_export_data.py
├── 15_batch_insertion.py
├── 16_basic_transaction_handling.py
├── 17_updating_multiple_tables_in_a_transaction.py
├── 18_batch_inserts_with_transaction.py
├── 19_transactional_banking_operations.py
├── 20_1_fix_add_stock_column.py
└── 20_inventory_management_transaction.py
```

---

## 🧪 Basic SQLite3 Installation & Testing

### 🔧 Setup

Install SQLite locally:

```bash
sudo apt install sqlite3
```

### 🧬 Testing

```bash
sqlite3 example.db
```

```sql
CREATE TABLE COMPANIES (company_name varchar(20), id int);
INSERT INTO COMPANIES VALUES ("aganitha", 1);
```

Exit using `.exit` or `Ctrl+D` and validate using:

```bash
file example.db
```

📸 Screenshot:
![Database Output](database_output.png)

---

## 🚀 Project Modules & Highlights

### 1. 📁 Basic DB Creation & Operations

* `1_create_store_db.py`: Creates `store.db` if it doesn't exist.
* `2_create_products_table.py`: Sets up `products` table.
* `3_insert_product.py`: Function to insert product.
* `4_read_products.py`: Reads and prints all products.
* `5_update_product_price.py`: Updates product price by ID.
* `6_delete_product.py`: Deletes product by ID.

### 2. 🧱 OOP for DB

* `7_product_class.py`: Class to encapsulate product operations.

### 3. 🛡️ Exception Handling

* `8_product_with_exceptions.py`: Adds try-except blocks for robustness.

### 4. 🔍 Search Functionality

* `9_search_product_by_name.py`: Partial name matching.

### 5. ✅ Data Validation

* `10_product_with_validation.py`: Ensures valid product input.

### 6. 🔄 Transactions

* `11_using_transactions.py`: Wraps operations in transactions.

### 7. 🔗 Join Queries

* **Folder: `12_join_queries/`**

  * `12_create_tables.py`: Creates `products` & `categories` with FK.
  * `12_insert_sample_data.py`: Sample data insertion.
  * `12_product_class.py`: JOIN query to get product with category.

### 8. 📊 Aggregation

* `13_aggregation_queries.py`: Calculates total product value.

### 9. 📄 Exporting Data

* `14_export_data.py`: Export products to CSV (`products_data.csv`).

### 10. 📅 Batch Insertion

* `15_batch_insertion.py`: Inserts multiple records efficiently.

### 11. 🦾 Basic Transaction Handling

* `16_basic_transaction_handling.py`: Rollback on error demo.

### 12. 🔄 Multi-table Transaction

* `17_updating_multiple_tables_in_a_transaction.py`: Sync multiple tables atomically.

### 13. 📦 Batch Insert with Transactions

* `18_batch_inserts_with_transaction.py`: One transaction for batch.

### 14. 💰 Transactional Banking Operations

* `19_transactional_banking_operations.py`: Transfer funds example with rollback.

### 15. 🏷️ Inventory Management with Transactions

* `20_1_fix_add_stock_column.py`: Schema update for stock column.
* `20_inventory_management_transaction.py`: Atomically updates inventory and logs.

---

## 🧠 Concepts Covered

| Concept            | Description                              |
| ------------------ | ---------------------------------------- |
| Transactions       | Grouping operations for atomicity        |
| ACID Properties    | Ensures data consistency and reliability |
| CRUD               | Create, Read, Update, Delete operations  |
| SQL Joins          | Combining tables using keys              |
| Batch Processing   | Insert multiple rows efficiently         |
| CSV Export         | Extracting structured data               |
| Exception Handling | Robust operations with rollback support  |

---

## ▶️ Running the Project

1. **Clone the repository**

   ```bash
   git clone https://github.com/yamini-Krishna/bootcamp.git
   cd persistence-drills
   cd using_sqlite_with_python
   ```

2. **Set up the environment**
   Install required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run modules individually**
   Start with database creation:

   ```bash
   python 1_create_store_db.py
   python 2_create_products_table.py
   python 3_insert_product.py
   ```

   Explore advanced modules such as:

   ```bash
   python 11_using_transactions.py
   python 13_aggregation_queries.py
   python 14_export_data.py
   ```

4. **Run Join Query Folder**
   Navigate to the join queries folder:

   ```bash
   cd 12_join_queries
   python 12_create_tables.py
   python 12_insert_sample_data.py
   python 12_product_class.py
   ```







