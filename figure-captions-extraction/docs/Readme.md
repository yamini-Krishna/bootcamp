
## 📘 Project Documentation with MkDocs

---

### 🛠️ Prerequisites

Ensure you have **Python 3.7+** installed, then install MkDocs:

```bash
pip install mkdocs
```

---

### 🚀 Getting Started

#### 1. Initialize MkDocs in your project

```bash
mkdocs new .
```

> This creates a `mkdocs.yml` configuration file and a `docs/` folder.

#### 2. Move your existing `README.md` (or create a new one)

Save your current `README.md` in the `docs/` folder or edit the default `index.md` file.

Example:

```bash
mv README.md docs/index.md
```

#### 3. Serve the documentation locally

```bash
mkdocs serve
```

📂 Open your browser and navigate to:

```
http://127.0.0.1:8000
```

You’ll see your documentation rendered live!

---

### 📦 Build Static Site

To generate the static HTML site:

```bash
mkdocs build
```



