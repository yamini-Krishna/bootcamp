# 🔐 Python Persistence Drill Series

Welcome to the **Python Persistence Drill Series** — a comprehensive collection of serialization and deserialization exercises. These hands-on tasks are designed to give you practical mastery over object persistence using `pickle`, `json`, `yaml`, and custom techniques in Python.


---

## 📁 Project Structure

| File / Module                      | Description                                               |
| ---------------------------------- | --------------------------------------------------------- |
| `1_pickle_serialize_person.py`     | Serialize a `Person` object using `pickle`.               |
| `2_pickle_deserialize_person.py`   | Deserialize the `Person` object from a pickle file.       |
| `3_json_serialization.py`          | Convert a `Book` object to a JSON string.                 |
| `4_json_deserialization.py`        | Create a `Book` instance from a JSON string.              |
| `5_yaml_serialization.py`          | Serialize a `Car` object into YAML using PyYAML.          |
| `6_yaml_deserialization.py`        | Deserialize a `Car` object from a YAML string.            |
| `7_1_graph_serialize.py`           | Custom serialization of a `Graph` with nodes and edges.   |
| `7_2_graph_deserialize.py`         | Deserialize the `Graph` object back to memory.            |
| `8_user_serialize.py`              | Serialize a `User` object excluding sensitive attributes. |
| `9_1_game_save.py`                 | Save the state of a game session to a file.               |
| `9_2_game_load.py`                 | Restore the saved game state.                             |
| `10_1_profile_save.py`             | Save profile with version 1 structure.                    |
| `10_2_profile_load.py`             | Load and handle versioned profile data.                   |
| `11_1_mycollection_serialize.py`   | Serialize a custom collection class `MyCollection`.       |
| `11_2_mycollection_deserialize.py` | Deserialize and restore `MyCollection` from file.         |
| `12_1_cycle_serialize.py`          | Serialize objects with cyclic references.                 |
| `12_2_cycle_deserialize.py`        | Safely load objects with circular references.             |
| `person.py`                        | Contains the `Person` class used in drills 1 & 2.         |
| `requirements.txt`                 | External dependencies (e.g., `pyyaml`).                   |

---

## 📂 Sample Serialized Files

These are binary files created during serialization:

* `person.pkl` – Serialized Person object
* `profile.pkl` – Versioned profile state
* `game_state.pkl` – Saved game session
* `my_collection.pkl` – Custom collection object
* `cyclic_objects.pkl` – Cyclic reference sample

---

## 📦 Installation & Setup

1. **Clone this repository**

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run any drill file**

   ```bash
   python 1_pickle_serialize_person.py
   ```

---

## 🧰 Skills You'll Learn

* 🔹 Python's `pickle`, `json`, and `yaml` modules
* 🔹 Working with custom and nested data structures
* 🔹 Securing sensitive data during serialization
* 🔹 Object versioning and backward compatibility
* 🔹 Handling cyclic object references
* 🔹 File I/O best practices

---

## 📘 Learning Reference

Official Python documentation:
🔗 [https://docs.python.org/3/library/persistence.html](https://docs.python.org/3/library/persistence.html)

---

## 🧠 Why This Matters

Persistence is a foundational skill for:

* Saving application state
* Game development
* Machine learning model storage
* Config file generation and parsing
* Inter-process communication
* Data migration and backups

Mastering these concepts ensures you’re ready to build resilient, maintainable, and scalable Python applications.


