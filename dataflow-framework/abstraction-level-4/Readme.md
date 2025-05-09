 🌀 Level 4 – Stream Processing and State

This level upgrades the dataflow framework from simple `str -> str` functions to full **stream-based processing**, enabling real-world features like:

- ✅ Fan-out (splitting one line into multiple)
- ✅ Fan-in (merging multiple lines into one)
- ✅ Stateful processing (line counters, buffers)
- ✅ Configurable and reusable processors

---

## 📂 Project Structure

```

abstraction-level-4/
├── main.py                # Entry point: runs sample pipelines
├── processors.py          # All stream processors implemented here
├── test\_processors.py     # Unit tests (optional)
└── requirements.txt       # (If any dependencies are needed)

````

---

## 🚀 How to Run

### ▶️ Run the Main Program
```bash
python main.py
````

This will display output from:

* Simple uppercase processor
* Stateful line counter
* Fan-in processor (joins every 2 lines)
* Fan-out processor (splits on delimiter)

### 🧪 Run Tests

If `test_processors.py` exists:

```bash
python -m unittest test_processors.py
```

---

## 🛠️ Processors Implemented

| Processor                | Type                     | Description                             |
| ------------------------ | ------------------------ | --------------------------------------- |
| `simple_processor`       | Stateless                | Converts each line to uppercase         |
| `line_counter_processor` | Stateful                 | Adds line number (e.g., `Line 1: text`) |
| `fan_in_processor`       | Stateful                 | Joins every two lines into one          |
| `fan_out_processor`      | Stateless / Configurable | Splits each line on a delimiter         |

---

## 🔁 Stream Interface

All processors follow this new interface:

```python
def processor_name(lines: Iterator[str]) -> Iterator[str]
```

You can now:

* Yield **zero, one, or many** lines per input
* Maintain internal **state**
* Create processors with **initial parameters** using classes or closures

---

## 🔄 Reusing Old `str -> str` Functions

Use a decorator to convert simple processors:

```python
def line_processor(func: Callable[[str], str]) -> Callable[[Iterator[str]], Iterator[str]]:
    def wrapped(lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield func(line)
    return wrapped
```

---

## ✅ Level 4 Goals Checklist

* [x] All processors support `Iterator[str] -> Iterator[str]`
* [x] Wrapped/reused old `str -> str` functions
* [x] Fan-out and fan-in processors implemented
* [x] At least one stateful processor
* [x] Processors support initialization/config
* [x] All processors testable in isolation

---

## 📦 Requirements

If needed:

```bash
pip install -r requirements.txt
```

---

## 🔜 Next Level Preview

* DAG-based processing
* Conditional routing
* Multi-path pipelines

