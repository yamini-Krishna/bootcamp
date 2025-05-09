# Level 0 – Basic Script (No Abstraction)

## Overview

In this task, we create a basic Python script (`process.py`) that processes input data by reading it line by line, stripping whitespace, converting it to uppercase, and printing the processed output. This script serves as the starting point for further improvements in later levels.

## Task Details

### Requirements:

* Read input data line by line from `stdin`.
* Strip leading and trailing whitespace from each line.
* Convert each line of text to uppercase.
* Print the processed lines to `stdout`.

### Constraints:

* The script should be written sequentially, top to bottom (no functions).
* Only Python's built-in tools should be used.

### File Structure:

The project follows a simple file structure:

```
level-0-basic-script/
├── process.py  # The main script that processes input and produces output
└── input.txt   # Sample input file (optional for testing)
```

## Usage Instructions

1. **Run the Script:**

   * The script `process.py` reads from `stdin`. To test it with a file, run the following command:

     ```bash
     python process.py < input.txt
     ```

     This command will process the contents of `input.txt`, strip whitespace, and convert text to uppercase.

2. **Expected Output:**
   If the input file (`input.txt`) contains:

   ```
   Hello, World!
   This is a test.
   Python is awesome!
   ```

   The output should be:

   ```
   HELLO, WORLD!
   THIS IS A TEST.
   PYTHON IS AWESOME!
   ```

3. **Manual Input:**

   * If you prefer to provide input manually, run:

     ```bash
     python process.py
     ```

   * Then, type your input directly into the terminal. Press `Ctrl + D` to finish and see the processed output.

## Checklist

* [ ] Does the script process the input file correctly?
* [ ] Does the script produce the expected output when the input is passed through `stdin`?
* [ ] Does the script handle whitespace and convert text to uppercase as required?
* [ ] Has the code been written sequentially, with no functions used?
* [ ] Does the script run without errors when executed from the command line?

## Reflection

This script represents the first step in building a more complex system, where the focus is on simple, top-to-bottom code without abstraction. In future levels, we'll work on improving this script by introducing better structure, error handling, and abstraction.



