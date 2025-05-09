# Level 2 – Modular Structure and Standardized Processing

## Overview

This level refactors the script into a modular program, with clearly separated responsibilities. We also standardize the processor functions, allowing transformations to be composed into a pipeline.

---

## Task Details

### 1. Split Code into Modules

* **`main.py`**: Reads input and writes output.
* **`cli.py`**: Handles the CLI with **Typer**.
* **`core.py`**: Contains processor functions like `to_uppercase`, `to_snakecase`.
* **`pipeline.py`**: Assembles the list of processors based on the mode.
* **`types.py`**: Defines the `ProcessorFn` type (`Callable[[str], str]`).

### 2. Processor Functions

In `core.py`, implement processors:

* **`to_uppercase(line: str) -> str`**: Converts text to uppercase.
* **`to_snakecase(line: str) -> str`**: Converts spaces to underscores and changes to lowercase.

### 3. Build a Static Pipeline

In `pipeline.py`, create a static pipeline of processors based on the selected mode (`uppercase` or `snakecase`).

### 4. CLI with Typer

The CLI should support:

* `--input`: Input file path (required).
* `--output`: Output file path (optional).
* `--mode`: Processing mode (`uppercase` or `snakecase`).

---

## Project Structure

```
abstraction-level-2/
├── main.py         # Main logic (input/output)
├── cli.py          # CLI interface
├── core.py         # Processor functions
├── pipeline.py     # Pipeline assembly
└── types.py        # Type definitions
```

---

## Setup Instructions

Install dependencies:

```bash
pip install typer python-dotenv
```

---

## Usage

1. **Default Mode (Uppercase)**

   ```bash
   python process.py --input input.txt
   ```

2. **Snakecase Mode**

   ```bash
   python process.py --input input.txt --mode snakecase
   ```

3. **Output to File**

   ```bash
   python process.py --input input.txt --output output.txt
   ```

---

## Checklist

* [ ] Are modules split as described?
* [ ] Is the processor type `ProcessorFn` used consistently?
* [ ] Can you add a new processor easily?
* [ ] Does the pipeline process lines sequentially?
* [ ] Does the CLI work with `--input`, `--output`, and `--mode`?

