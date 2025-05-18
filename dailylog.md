# 🗓️ `daily-log.md`

# day0 

## tools
```markdown

- Created `bootcamp` monorepo on GitHub.
- Set up Azure VM using GitHub Student Pack.
- Installed Docker and tested Python container.
- Configured SSH keys for GitHub and server login.
- Installed `uv`, Python 3.13 and 3.11, and created virtual environment.
- Set up basic web server with name and photo.
- Installed and tested `rsync` for file transfers.
- Installed Asciinema for CLI recording.
```

---

## basics

```markdown

-  Initialized Python project with `uv init`
-  Created virtual env (Python 3.13) using `uv venv`
-  Configured IDE (VS Code) to use virtual env
-  Created module `yamini-hello` to greet passed argument
-  Published module on TestPyPI
-  Installed and used `rich` to print styled output
-  Installed and used `typer` to make it a CLI app
-  Registered CLI command in `pyproject.toml`
-  Recorded demo via Asciinema for CLI app
-  Completed typing drills (functions, list, dict, Optional, Union, Callable, TypedDict)
-  Practiced IDE features: type checking, linting, refactoring, navigation, renaming, docstrings, and import management
```

---
# day1 

## doctools

```markdown
**What I learned:**
- Markdown basics (headings, links, code, lists)
- How docs help teams work better
- Setup MkDocs project

**What confused me:**
- How to add diagrams in MkDocs

```

---

# day2

## language-drills

```
- Mastered Python basics: lists, dicts, sets, tuples, comprehensions, functions, scope, error handling, iterators, and generators.
- Explored Pythonic idioms: EAFP vs LBYL, built-in functions, inline expressions, context managers.
- Practiced OOP: classes, inheritance, magic methods, data classes, static/class methods.
- Used functional tools: lambdas, decorators, functools, itertools.
- Navigated the standard library: collections, filesystem, datetime, JSON/CSV/pickle, subprocess.
- Learned data validation: pydantic, field metadata, logging, naming.
- Covered performance/debugging: profiling, lazy evaluation, debugging tools, observability, packaging.
```

---

# dataflow-framework

- Completed all abstraction levels from 0 to 7:
  -  Level 0: Basic one-time line processing script.
  -  Level 1: Added CLI arguments and environment config.
  -  Level 2: Modularized code with str → str processors.
  -  Level 4: Implemented stream processing with stateful logic.
  -  Level 5: Built a DAG-based routing system.
  -  Level 6: Designed a tag-based state transition engine.
  -  Level 7: Added observability with metrics and line tracing.
- Wrapped up with `FINAL.md` summarizing the architecture and learnings.

### Key Learnings

- How to evolve a simple script into a reusable system.
- Managing complexity with abstraction and modularity.
- Building a routing engine with condition-based flow.
- Adding real-time observability to track internal operations.

---

# persistence-drills

#### Folder 1: File Serialization

* Used `pickle`, JSON, and YAML for serializing custom classes.
* Handled advanced cases: cyclic refs, versioning, sensitive data, game state saving.

#### Folder 2: SQLite Basics

* Learned ACID properties, SQLite reliability, and use case scenarios.

#### Folder 3: System Setup

* Installed SQLite, created tables, exported DB files.
* Wrote program to generate 500 SQL inserts efficiently.

#### Folder 4: SQLite3 with Python

* Implemented CRUD and transactions on `store.db`.
* Managed categories, batch inserts, exports, and simulated banking transactions.

#### Folder 5: SQLAlchemy + Pydantic

* Built ORM models and schemas.
* Performed CRUD, relationships, bulk inserts with rollback.
* Converted code to async.

#### Folder 6: Real-World Drills

* Added schema migrations (e.g., `created_at`).
* Implemented soft deletes, audit logging, rate limiting, and recovery.







