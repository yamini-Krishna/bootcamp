

---

```markdown
# Section 7.5 – Packaging with `pyproject.toml`

This module demonstrates how to package a Python project using `pyproject.toml`, define an entry point for command-line usage, build a wheel, and install/test the package locally.

---

## 📁 Project Structure

```

mytool/

├── **init**.py

├── cli.py

├── data/

      └── sample.txt

pyproject.toml

README.md

````

---

## 📌 Steps Covered

### 1. Minimal Project File
Defines project metadata and build system.

```toml
[project]
name = "mytool"
version = "0.1.0"
...

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
````

---

### 2. Define CLI Entry Point

Expose a command-line interface via `pyproject.toml`.

```toml
[project.scripts]
mytool = "mytool.cli:main"
```

In `cli.py`:

```python
def main():
    print("Hello from mytool!")
```

Usage after install:

```bash
mytool
# Output: Hello from mytool!
```

---

### 3. Build the Package

```bash
python -m build
```

Creates:

* `dist/mytool-0.1.0-py3-none-any.whl`
* `dist/mytool-0.1.0.tar.gz`

---

### 4. Install Locally

```bash
pip install dist/mytool-0.1.0-py3-none-any.whl
```

---

### 5. Include Extra Files

```toml
[tool.setuptools.package-data]
"mytool" = ["data/*.txt"]
```

Ensures text/data files are included in the distribution.

---

### 6. Versioning Strategy

Supports:

* `0.1.0`
* `0.1.0-alpha`
* Dynamic versioning via Git tags

---

### 7. Test Installed Package

```python
import mytool.cli
mytool.cli.main()
```

---




