# **Level 5 – DAG Routing and Conditional Flows**

## **Overview**

In this level, we extend the processing system to handle more complex scenarios using a **Directed Acyclic Graph (DAG)** for routing and conditional flows. Unlike previous levels where every line followed the same processing flow, in this level, we introduce the concept of **conditional routing** where each line can be routed to different processors based on its content or tags. This allows for more flexible, real-world processing scenarios such as log processing, where different types of logs require different handling.

### **Key Concepts**:

* **DAG (Directed Acyclic Graph)**: A structure where each processor is a node, and the flow between nodes is directed. Lines can be routed to different processors based on tags or conditions.
* **Conditional Routing**: Lines are tagged based on content (e.g., ERROR, WARNING, INFO), and routed to different processors according to these tags.
* **Tagging**: Each line is tagged by the processor before being routed to its downstream processors.

---

## **Motivating Example: Log Routing**

Imagine you're building a log processing tool. Each log line might be:

* An **ERROR** that needs to be logged separately.
* A **WARNING** to be counted.
* A **GENERAL** message to simply pass through.

### **Desired Flow**:

1. **Trim Processor**: Each line is passed through a trim processor to remove any extra spaces or leading/trailing whitespace.
2. **Tagging Processor**: After trimming, lines are tagged with labels like `tag_error`, `tag_warn`, or `tag_info` based on their content.
3. **Routing**: A router sends the lines to different branches:

   * **Errors** are processed by the error handler (count and archive).
   * **Warnings** are sent to a tally processor.
   * **General messages** are formatted and printed.

---

## **How it Works**

1. **Input**: A list of log lines (or any other data lines) are provided in the `main.py` file.
2. **Processing Pipeline**:

   * The lines are processed through a series of **processors**.
   * Each processor either processes the line or tags it with additional information (like `error`, `warning`, `info`).
   * Based on the tag, lines are routed to different downstream processors.

---

## **How to Run the Pipeline**

### **1. Set up a Virtual Environment**

Before running the pipeline, make sure you have set up a virtual environment to manage dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### **2. Install Required Dependencies**

If the project has any dependencies (like `numpy`, `pandas`, etc.), install them using `pip`:

```bash
pip install -r requirements.txt
```

### **3. Running the Pipeline**

To run the DAG processing pipeline, simply execute the `main.py` file. This will trigger the flow where lines are processed by different processors based on their content and routing configuration.

```bash
python main.py
```

---

## **How the Pipeline Works**

### **1. `main.py`**: Input & Execution

The `main.py` file defines the input lines and initiates the DAG execution using the `run_dag` function from `engine.py`. It provides the input log lines and the starting processor (in this case, `trim`).

### **2. `config.py`**: Configuration

The `config.py` file contains the configuration for the pipeline:

* It defines the processors used in the DAG.
* It includes routing information, specifying which processor a line should be routed to based on the tags assigned (e.g., error lines are routed to the error processor).

### **3. `processors.py`**: Processors

The `processors.py` file contains various processor functions that process the lines. For example:

* `trim_processor`: Removes extra spaces.
* `tag_processor`: Tags lines based on their content (ERROR, WARNING, etc.).
* Other processors can handle specific tasks like counting errors, formatting messages, or tallying warnings.

### **4. `engine.py`**: DAG Execution Engine

The `engine.py` file is the core of the DAG engine. The `run_dag` function uses the configuration in `config.py` to route the lines through the processors based on their tags. The engine manages the flow of lines through the system.

---

## **Customizing the Input**

In the `main.py` file, you can modify the `input_lines` list to test different inputs. For example:

```python
input_lines = [
    "ERROR: system crash",
    "WARNING: disk space low",
    "INFO: system running smoothly"
]
```

By adjusting the input lines, you can simulate different types of log messages and see how the system processes and routes them.

---

## **Expected Output**

Based on the routing configuration, here's an example of what the output could look like:

```bash
Trimmed: ERROR: something failed
Trimmed: WARNING: check this setting
Trimmed: INFO: all good

Error log: ERROR: something failed
Warning log: WARNING: check this setting
Formatted log: INFO: all good
```

### **Possible Error Handling**

If something goes wrong during processing, the program may raise an exception. You can modify the error handling logic as needed to catch and handle specific errors in your pipeline.

---

## **Testing the Pipeline**

To test your DAG processing pipeline, simply modify the input lines or the processor configuration. You can also extend the pipeline by adding more processors or adjusting the routing rules.

---

## **Conclusion**

This level introduces **DAG routing** and **conditional flows** to the processing pipeline, making it more flexible and adaptable to real-world scenarios like log processing. With the ability to route lines based on content and tags, the system can handle complex workflows efficiently.


