
# State-Based Routing System 

A general-purpose state transition engine designed to dynamically route lines through processors based on tags. The system behaves like a state machine or router, where processors represent states, and transitions between states are triggered by tags.

---

## 🧩 Core Ideas

- **Tags as State Labels:** Lines are processed and tagged at each step.
- **Dynamic Routing:** The path a line takes is based on its tag.
- **Cyclic Flow Support:** Supports cycles in routing, allowing for more complex workflows.
- **Modular Processors:** Processors are modular and reusable, with each processor defined as a callable object or class.
- **Fan-Out and Fan-In:** A line can take multiple paths (fan-out) or converge from multiple sources (fan-in).

---

## 🔧 System Requirements

Before running the system, make sure you have Python 3.x installed. You can install the dependencies using the following:

1. Clone this repository:
   ```bash
   git clone https://github.com/yamini-Krishna/bootcamp.git
   cd bootcamp/dataflow-framework/abstraction-level-6
```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🏗️ Project Structure

```
state-based-routing/
├── config.py           # Configuration file for tag-to-processor mappings
├── engine.py           # Core engine for routing and managing state transitions
├── processors/         # Directory for processor modules
│   ├── __init__.py     # Marks the directory as a Python package
│   ├── start.py        # 'start' tag processor
│   ├── filters.py      # Filter processors (e.g., error, warning filters)
│   ├── formatters.py   # Format processors (e.g., convert text to snake_case)
│   └── output.py       # Output processors (e.g., terminal output)
├── main.py             # Entry point of the system
├── requirements.txt    # List of Python dependencies
└── README.md           # Project documentation (this file)
```

---

## 🚀 Getting Started

1. **Configuration**:

   * The `config.py` file defines the available processors and their mappings to tags. You can easily add new processors and configure them here.
   * The configuration follows the pattern where each tag is associated with a processor module.

   Example configuration snippet from `config.py`:

   ```python
   CONFIG = {
       "start": "processors.start.tag_lines",
       "error": "processors.filters.only_error",
       "warn": "processors.filters.only_warn",
       "general": "processors.formatters.snakecase",
       "end": "processors.output.terminal"
   }
   ```

2. **Running the system**:

   * To run the system, use the `main.py` file as the entry point:

     ```bash
     python main.py
     ```

   * The `main.py` will start the system by passing the input lines through the processors based on their tags. The flow continues until an `end` tag is encountered.

---

## 🔄 Workflow Example

Here's an example scenario of how the system routes lines:

1. **Start Processor (`processors.start.tag_lines`)**:

   * The `start` processor takes lines tagged with `'start'`.
   * It emits new tags like `'error'`, `'warn'`, or `'general'`.

2. **Filter Processors (`processors.filters.only_error`, `processors.filters.only_warn`)**:

   * Lines tagged as `'error'` pass through `only_error`.
   * Lines tagged as `'warn'` pass through `only_warn`.

3. **Formatter Processor (`processors.formatters.snakecase`)**:

   * Lines tagged as `'general'` go through the `snakecase` formatter to convert text.

4. **Output Processor (`processors.output.terminal`)**:

   * When a line reaches the `'end'` tag, it is passed to the terminal output.

---

## 💡 Features

* **Dynamic Routing**: Lines flow through processors based on their tags.
* **Multiple Routes (Fan-Out)**: One line can trigger multiple processors.
* **Cyclic Support**: Tags can loop, allowing for retry mechanisms.
* **Configurable**: Easily modify the tag-to-processor mapping in `config.py`.
* **Modular Processors**: Add new processors without changing the core logic.

---

## 🛠️ Customizing the System

### 1. **Adding a New Processor**

To add a new processor:

* Create a new Python file in the `processors/` directory.
* Define a class or function with the signature:

  ```python
  def process(self, lines: Iterator[Tuple[str, str]]) -> Iterator[Tuple[str, str]]:
      # Your processing logic
      yield new_tag, processed_line
  ```

### 2. **Update Configuration**

To add a new processor to the routing system, update `config.py` with the new tag and processor mapping:

```python
"new_tag": "processors.new_processor.module_name"
```

---

## ⚠️ Guarding Against Infinite Loops

In a state machine, infinite cycles might occur. The system should detect or limit infinite loops in routing. You can implement safeguards inside `engine.py` to ensure that if a tag keeps looping back to itself, the system will halt after a specified number of iterations.

---

## 📝 Reflection

This system can handle complex workflows where tags dynamically determine the processing path. You can implement retry mechanisms, feedback loops, and sophisticated workflows with this flexible framework.

In a distributed setting, this system can be scaled across multiple machines where processors are distributed and run in parallel, improving efficiency and fault tolerance.



