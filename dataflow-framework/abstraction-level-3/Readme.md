# Level 3 – Dynamic Config-Driven Pipeline

## Overview

In this level, the pipeline logic is decoupled from the code by loading processing steps dynamically from a configuration file (`pipeline.yaml`). This enables users to customize and extend the pipeline with minimal changes to the core code, fostering extensibility and flexibility.

---

## Task Details

### Key Changes:

1. **Dynamic Pipeline via YAML:**

   * Replace the static pipeline from Level 2 with a dynamic one defined in a YAML file.
   * The `pipeline.yaml` file specifies a sequence of processors using dotted import paths, allowing users to define their own processing logic without modifying the code.

2. **Processor Functions:**

   * Functions like `to_uppercase` and `to_snakecase` are loaded dynamically based on the YAML configuration.

3. **CLI Update:**

   * Modify the CLI to accept a `--config` argument, replacing the `--mode` argument, to load the pipeline configuration from a YAML file.

4. **Dynamic Function Loading:**

   * Implement a function that parses the `pipeline.yaml` file, loads processor functions using Python’s `importlib`, and returns a list of processor functions to be applied to the input.

---

## Project Structure

```
abstraction-level-3/
├── main.py         # Main script to read input and process output
├── cli.py          # CLI interface using Typer
├── core.py         # Contains processor functions like to_uppercase, to_snakecase
├── pipeline.py     # Assembles pipeline from YAML config
├── types.py        # Type definitions for ProcessorFn
├── processors/     # Contains processor functions (e.g., upper.py, snake.py)
│   ├── upper.py    # Processor for uppercase conversion
│   └── snake.py    # Processor for snake_case conversion
└── pipeline.yaml   # YAML config file specifying processing steps
```

---

## Key Concepts

1. **YAML Configuration**
   The `pipeline.yaml` defines the processing steps in the form of dotted import paths. For example:

   ```yaml
   pipeline:
     - type: processors.snake.to_snakecase
     - type: processors.upper.to_uppercase
   ```

2. **Dynamic Loading of Processors**
   The program dynamically imports each processor using the import path defined in the YAML configuration. This is done at runtime using Python’s `importlib`.

3. **Processor Function Type**
   All processors must conform to the signature `str -> str`. Each processor function transforms a string (e.g., converts text to uppercase or snake\_case).

4. **CLI Update**
   The CLI now accepts a `--config` argument to load the configuration from a YAML file:

   ```bash
   python main.py --input input.txt --config pipeline.yaml
   ```

---

## Setup Instructions

### Install Dependencies

Ensure you have the necessary Python libraries installed:

```bash
pip install typer python-dotenv
```

---

## Usage

1. **Run the Program**
   To process a file using the dynamic pipeline defined in `pipeline.yaml`:

   ```bash
   python main.py --input input.txt --config pipeline.yaml
   ```

   This command processes the `input.txt` file using the pipeline specified in the `pipeline.yaml` file and outputs the result.

2. **Example YAML (`pipeline.yaml`)**
   Here’s an example of how the YAML file defines the processing pipeline:

   ```yaml
   pipeline:
     - type: processors.snake.to_snakecase
     - type: processors.upper.to_uppercase
   ```

---

## Checklist

* [ ] Has the CLI been updated to accept a config file (`--config`)?
* [ ] Does the program dynamically load and compose processor functions from the YAML configuration?
* [ ] Do all processor functions conform to the `str -> str` signature?
* [ ] Are import errors handled cleanly with clear error messages?
* [ ] Does `pipeline.yaml` specify functions using full dotted import paths?

---

## Reflection

With this level, your code is now flexible enough to allow users to define and extend the pipeline without modifying the source code. Future improvements can include:

* **Third-party plugins:** Allow users to create custom processors and plug them into the pipeline.
* **Guardrails:** Consider adding validation and logging to ensure robustness when loading and applying processors dynamically.

---

This approach introduces a powerful, flexible way to handle transformations and prepares the program for future enhancements, such as stream-based processing or more complex workflows.


