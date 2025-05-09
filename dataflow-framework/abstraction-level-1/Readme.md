# Level 1 – Parameters and CLI Interface

## Overview

In this level, we improve the basic script by transforming it into a parameterized tool. The script now accepts command-line arguments, loads default values from an environment file, and processes files based on a configurable mode. This step sets us up for building reusable tools by making the script more flexible and user-friendly.

## Task Details

### Refactor the Script to:

1. **Use Typer to define a command-line interface (CLI)**:

   * The script should accept `--input`, `--output`, and `--mode` as command-line arguments.
   * The `--mode` parameter will be used to select the processing behavior (e.g., converting text to uppercase or snake case).
   * Use **python-dotenv** to load default values (e.g., the default mode) from a `.env` file.

2. **Modes of Processing**:

   * **uppercase**: Convert each line to uppercase.
   * **snakecase**: Replace spaces with underscores and convert the text to lowercase.
   * The script should default to **uppercase mode** if no mode is provided, by using the value from the `.env` file.

3. **Functionality Breakdown**:

   * Read the input lines from the file.
   * Process each line based on the selected mode.
   * Write the processed lines either to an output file or print them to stdout.

### Functionality Breakdown

We will introduce the following functions:

* **`read_lines(path: str) -> Iterator[str]`**:

  * Reads the lines from the input file.
* **`transform_line(line: str, mode: str) -> str`**:

  * Transforms the line based on the selected mode (`uppercase` or `snakecase`).
* **`write_output(lines: Iterator[str], output_path: Optional[str]) -> None`**:

  * Writes the transformed lines either to a specified output file or prints them to the console.

---

## File Structure

The project structure will look like this:

```
level-1-parameters-cli/
├── process.py        # The main script with Typer CLI interface
├── .env              # Environment file for default mode
├── input.txt         # Sample input file (optional for testing)
└── output.txt        # Optional output file
```

---

## Setup Instructions

### 1. Install Required Dependencies

Before running the script, ensure that you have installed the required dependencies. You can install them using `pip`:

```bash
pip install typer python-dotenv
```

### 2. Create `.env` File

The `.env` file contains default values for the script. In this case, it will specify the default processing mode:

```ini
MODE=uppercase
```

You can adjust this file to use `snakecase` as the default mode if needed.

---

## Usage Instructions

### 1. Run the Script

#### Process with Default Mode (Uppercase)

To run the script with the default `uppercase` mode, use:

```bash
python process.py --input input.txt
```

This will read the content from `input.txt`, convert each line to uppercase, and print the result to the console.

#### Process with a Specific Mode

To change the processing mode to `snakecase`, run:

```bash
python process.py --input input.txt --mode snakecase
```

This will replace spaces with underscores and convert the text to lowercase.

#### Output to a File

To write the results to an output file (`output.txt`), use:

```bash
python process.py --input input.txt --output output.txt
```

This will write the processed lines to `output.txt` instead of printing to the console.

### 2. Environment File

The script will default to the mode specified in the `.env` file (if `--mode` is not provided).

For example, if `.env` contains `MODE=uppercase`, the script will automatically convert the lines to uppercase unless overridden by `--mode`.

---

## Example Usage

1. **Uppercase Mode (default)**

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

4. **Specifying Mode in `.env`**

   If `.env` specifies `MODE=snakecase`, running the script without `--mode` will apply the snakecase transformation:

   ```bash
   python process.py --input input.txt
   ```

---

## Checklist

* [ ] Can the script process any file passed via `--input`?
* [ ] Does it default to `uppercase` mode via `.env`?
* [ ] Can you pass `--mode snakecase` to get a different transformation?
* [ ] Can the script print results to `stdout` or write to a file via `--output`?
* [ ] Is Typer used for a clean CLI?
* [ ] Is the logic divided into small functions (`read_lines`, `transform_line`, `write_output`)?

---

## Reflection

This level introduces a basic CLI tool with configurable parameters, preparing the way for more structured, reusable programs. Moving forward, we’ll separate out the logic into multiple files and continue improving the design for more complex use cases.



