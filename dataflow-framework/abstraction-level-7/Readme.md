
# **Metrics and Trace Dashboard for Data Processing System** 🌟

This project introduces **observability** and **introspection** to a data processing engine. It provides **real-time metrics**, **traces**, and **error logs** via a web dashboard built using **FastAPI**. The dashboard exposes live data about the processing system, allowing users to monitor the system’s performance and track individual lines' journeys through the processing pipeline.

## **Core Features** 🚀

* **Metrics Layer** 📊:

  * Counts of lines received and emitted per processor.
  * Processing time per processor.
  * Number of exceptions or retries encountered.

* **Execution Tracing** 🛤️:

  * Each line carries a trace of its journey through the system.
  * Traces of recent lines are stored and accessible.

* **Web Dashboard** 🌐:

  * Provides real-time access to metrics and logs via FastAPI.
  * Runs concurrently in a separate thread while the main processing continues.
  * Endpoints for `/stats`, `/trace`, and `/errors`.

* **Concurrency** ⚙️:

  * Uses threading and shared memory structures to maintain system responsiveness.

---

## **Setup Instructions** 🛠️

### Prerequisites 🔧

1. Python 3.x installed on your system.
2. Virtual environment setup for Python (recommended).
3. Dependencies installed via `requirements.txt`.

### 1. **Clone the repository** 🧑‍💻

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. **Set up the virtual environment** 🌱

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
.\venv\Scripts\activate  # For Windows
```

### 3. **Install dependencies** 📦

```bash
pip install -r requirements.txt
```

### 4. **Run the server** 🚀

Start the FastAPI server in the background:

```bash
python main.py --trace
```

* The server will run on `http://localhost:8000`.
* The `--trace` flag enables trace logging for each processed line.

### 5. **Visit the Web Dashboard** 📱

Once the server is running, you can visit the following endpoints in your browser:

* **Stats**: `http://localhost:8000/stats`

  * Provides live processor metrics: counts of processed lines, processing time, and errors.
* **Trace**: `http://localhost:8000/trace`

  * Displays recent traces showing the journey of processed lines.
* **Errors**: `http://localhost:8000/errors`

  * Lists recent errors, including processor names and messages.

---

## **Command-Line Arguments** 🎮

* **`--trace`**:

  * Enables tracing for each processed line. When enabled, the system tracks the journey of each line through the processing pipeline and stores recent traces.

---

## **Dashboard Endpoints** 🖥️

1. **`/stats`** - Live processor metrics 📊:

   * Shows how many lines were processed, the time taken, and the number of errors for each processor.
   * Example:

   ```json
   {
     "total_lines_processed": 3,
     "total_processing_time": 0.314,
     "total_errors": 1,
     "lines_processed_by_each_processor": {
       "general": 3
     }
   }
   ```

2. **`/trace`** - Recent traces of lines 🛤️:

   * Shows the most recent traces of processed lines, indicating the journey through the system.
   * Example:

   ```json
   {
     "recent_traces": ["general", "general", "general"]
   }
   ```

3. **`/errors`** - Recent error logs ⚠️:

   * Displays the most recent errors with the processor that caused them.
   * Example:

   ```json
   {
     "recent_errors": ["An error occurred"]
   }
   ```

---

## **System Overview** 🔍

The system is designed to process lines (e.g., log entries) through various processors, track metrics on how those lines are handled, and display this information on a live dashboard.

* **Metrics Tracking** 📊:

  * `total_lines_processed`: Total number of lines processed.
  * `total_processing_time`: Total time spent processing lines.
  * `total_errors`: Count of errors that occurred during processing.
  * `lines_processed_by_each_processor`: Dictionary of processor names with counts of processed lines.

* **Execution Tracing** 🛤️:

  * Each processed line carries trace data (e.g., `["start", "warn", "end"]`), indicating its journey through the system.
  * Traces are stored and can be accessed via the `/trace` endpoint.

* **Error Logs** ⚠️:

  * Errors encountered during processing are stored and can be accessed via the `/errors` endpoint.

---

## **Reflection** 💭

This project demonstrates the importance of system **observability**, enabling engineers, operators, and developers to:

* Track how records move through the system.
* Identify slow or error-prone components.
* Monitor the system’s performance in real-time.


