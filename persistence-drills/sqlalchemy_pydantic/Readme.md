
# SQLAlchemy & Pydantic Practice Repository

This repository contains a collection of practice exercises designed to help you get hands-on experience with **SQLAlchemy** ORM and **Pydantic** for data validation and serialization. The exercises progress from beginner to advanced, covering key concepts such as model creation, CRUD operations, query filtering, async database interactions, and more.

---

## 📂 Folder Structure

The project is structured as a series of Python scripts that follow a progressive learning path:

| File Name                       | Description                                                 |
| ------------------------------- | ----------------------------------------------------------- |
| `01_basic_model.py`             | Define SQLAlchemy models and create a database table.       |
| `02_insert_user.py`             | Insert user data into the database.                         |
| `03_fetch_users.py`             | Query user data from the database.                          |
| `04_filtering.py`               | Filter users by specific attributes.                        |
| `05_update_user.py`             | Update user records in the database.                        |
| `06_delete_user.py`             | Delete user records from the database.                      |
| `07_user_post_relationship.py`  | Establish relationships between users and posts.            |
| `08_nested_response.py`         | Create and return nested Pydantic models.                   |
| `09_bulk_insert_transaction.py` | Perform bulk insert operations with transactions.           |
| `10_async_sqlalchemy.py`        | Implement asynchronous database operations with SQLAlchemy. |

---

## 🚀 Prerequisites

Before running the scripts, ensure you have Python 3.10+ installed on your system.

Install the necessary dependencies using `pip`:

```bash
pip install sqlalchemy pydantic aiosqlite greenlet
```

* **SQLAlchemy**: ORM for database interactions.
* **Pydantic**: Data validation and serialization.
* **aiosqlite**: Async support for SQLite.
* **greenlet**: Required for async operations in SQLAlchemy.

---

## 📝 Overview of Exercises

### 1. **Basic Setup & CRUD Operations (Beginner)**

* **Define a simple SQLAlchemy model** and use **Pydantic** to define schemas for data validation.
* Perform **Insert**, **Fetch**, **Update**, and **Delete** operations on user data.

### 2. **Filtering & Querying Data (Intermediate)**

* Implement functionality to **filter users** by attributes (e.g., email).
* Use Pydantic models to structure the response data.

### 3. **Relationships & Nested Responses (Advanced)**

* Define relationships between models (e.g., a **User** can have multiple **Posts**).
* Retrieve a user and their related posts using **nested Pydantic models** for structured responses.

### 4. **Async Operations & Transactions**

* Leverage **async SQLAlchemy** operations for more efficient database interactions.
* Implement **bulk insertions** with transactions to ensure atomicity.

---

## 🏃‍♀️ How to Run

To run any of the exercises, simply execute the script using Python:

```bash
python3 01_basic_model.py
python3 10_async_sqlalchemy.py
```

Each script is standalone, and you can run them independently to see the results of each operation.

---

## ⚠️ Important Notes

* **SQLAlchemy 2.0 Update**:

  * The `declarative_base()` function is now available as `sqlalchemy.orm.declarative_base()` in version 2.0.

* **Pydantic v2 Update**:

  * In **Pydantic 2.x**, the config key `orm_mode` has been renamed to `from_attributes`. Make sure to adjust accordingly in the code.

* **Async Operations**:

  * For async scripts (`10_async_sqlalchemy.py`), ensure that **`aiosqlite`** and **`greenlet`** are installed, as they are required for handling async operations in SQLAlchemy.


