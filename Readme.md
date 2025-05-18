# day0

## tools

Basic setup for the bootcamp environment.

```markdown
- GitHub monorepo created.
- Linux server provisioned (Azure via GitHub Student Pack).
- Web server hosted with name and photo.
- Docker installed and tested with Python image.
- SSH keys configured for GitHub and server access.
- Rsync setup for local-to-server file transfers.
- Python 3.13 and 3.11 installed using `uv`.
- Virtual environment created using Python 3.13.
- Asciinema setup for CLI demos.
```

---

## basics

All exercises (`ex-basics-1`, `ex-basics-2`, `ex-basics-3`) were implemented in a single project folder.

```markdown
- Initialized project using `uv init` and created a virtual environment with `uv venv`
- Setup IDE (VS Code) with the created virtual environment
- Created a single module that:
  - Greets the passed argument or defaults to "world"
  - Uses `rich` to print a colorful message
  - Provides a CLI interface using `typer`
- Added CLI entry in `pyproject.toml`
- Published the package on TestPyPI  
- Recorded CLI usage demo with Asciinema  
 
 🛠️ Typing & IDE Drills (Practice)
- Explored static typing (functions, Optional, Union, Callable, etc.)
- Practiced VS Code features: type checking, linting, refactoring, navigation, renaming, and docstring preview
```

---

# day1

## doctools

````markdown
🧠 Developer Documentation Training

This repo tracks my progress through the Developer Documentation: Tools & Best Practices training.

📌 Purpose

To become fluent in writing and maintaining high-quality technical documentation using Markdown, diagrams, and tools like MkDocs.

🛠️ Setup

Install MkDocs and Material theme
pip install mkdocs-material

Preview the site locally
mkdocs serve

📎 Resources

* [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
* [Mermaid.js Docs](https://mermaid.js.org/)
* [Draw.io (diagrams.net)](https://draw.io/)

````

---

# day2

## language-drills

Python Learning Drills 🐍

Sections
Each section has hands-on drills with focused topics.

```markdown
1. Core Python (data structures, functions, error handling)
2. Pythonic Idioms (EAFP, built-ins, context managers)
3. OOP (classes, inheritance, data classes)
4. Functional Tools (lambdas, decorators, itertools)
5. Standard Library (collections, file I/O, JSON)
6. Validation & Clarity (pydantic, logging, naming)
7. Performance & Debugging (profiling, lazy eval, packaging)

```
---

# dataflow-framework

# Abstraction through Streaming Line Processing

## Overview
This project explores the evolution of a simple line-processing script into a modular, extensible, and observable streaming engine.

Each level increases in complexity, focusing on clean architecture, modularity, state handling, routing, and real-time observability.

## 📁 Project Structure

- `abstraction-level-0/`: Basic script, no abstraction.
- `abstraction-level-1/`: CLI arguments and environment config.
- `abstraction-level-2/`: Modular structure with standardized (str → str) processors.
- `abstraction-level-4/`: Stream-based processing and stateful transformations.
- `abstraction-level-5/`: DAG routing and conditional flows per line.
- `abstraction-level-6/`: Dynamic state-based routing using tags.
- `abstraction-level-7/`: Observability with metrics and a live dashboard.
- `FINAL.md`: Final project wrap-up, system design notes, and reflection.

## ✅ Goals

- Learn clean abstraction and separation of concerns.
- Build a flexible stream processing system.
- Route data based on content or state.
- Add observability like real-world systems.


