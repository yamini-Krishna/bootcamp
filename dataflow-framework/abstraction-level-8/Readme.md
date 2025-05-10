
# Dataflow Framework - Level 8

This is a data processing system that monitors a specified directory, processes text files, tracks metrics, and provides a real-time dashboard to visualize the progress and errors during processing.

## Features:

* **File Monitoring**: The system watches the `unprocessed` directory for new files and processes them sequentially.
* **Error Handling**: Logs errors encountered during processing and handles them gracefully.
* **Metrics Tracking**: Tracks the total number of lines processed, total processing time, errors encountered, and the number of lines processed by each processor.
* **Trace Logging**: Provides a trace log for each processed line, indicating its label (e.g., "info", "warn", "error").
* **Dashboard**: A real-time web dashboard that displays the system’s stats, trace logs, and recent errors.

## Directory Structure:

* `watch_dir/`

  * `unprocessed/`: Folder where new files to be processed are placed.
  * `underprocess/`: Folder where files are moved while being processed.
  * `processed/`: Folder where successfully processed files are moved.

## Requirements:

* Python 3.7+
* Required Python libraries:

  * `FastAPI`: Web framework for the dashboard.
  * `Uvicorn`: ASGI server for FastAPI.
  * `shutil`, `os`, `time`: For file handling and processing.

## Installation:

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd abstraction-level-8
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage:

### Watch Mode:

To start the system in watch mode (where it continuously monitors the `unprocessed` folder for new files):

```bash
python main.py --watch --trace
```

### Single File Mode:

To process a specific file:

```bash
python main.py --input <file_path> --trace
```

### Dashboard:

The system includes a web-based dashboard to monitor the stats and logs:

* **URL**: `http://0.0.0.0:8000`
* The dashboard includes endpoints to fetch stats, traces, and errors:

  * `/stats`: Displays metrics like total lines processed, errors, and processing time.
  * `/trace`: Displays recent trace logs of processed lines.
  * `/errors`: Displays recent errors encountered during processing.

### File Processing Flow:

1. Files are moved from the `unprocessed` folder to the `underprocess` folder.
2. The system processes each file line by line, categorizing them as "info", "warn", or "error".
3. Processed files are then moved to the `processed` folder.
4. Errors encountered during processing are logged, and metrics are updated in real time.

## Metrics:

* `total_lines_processed`: Total number of lines processed.
* `total_processing_time`: Total time spent processing all files.
* `total_errors`: Total number of errors encountered.
* `lines_processed_by_each_processor`: A breakdown of lines processed by each processor.
* `current_file`: The file currently being processed.
* `last_processed_files`: A list of recently processed files.

## Example Output:

### Stats:

```json
{
  "total_lines_processed": 5,
  "total_processing_time": 0.5245251655578613,
  "total_errors": 7,
  "lines_processed_by_each_processor": {},
  "current_file": null,
  "last_processed_files": ["sample_log_01.txt", "sample_log_02.txt"]
}
```

### Trace:

```json
{
  "recent_traces": ["info", "warn", "info", "warn", "info"]
}
```

### Errors:

```json
{
  "recent_errors": [
    "Sat May 10 09:46:41 2025: 'info'",
    "Sat May 10 09:46:41 2025: 'warn'",
    "Sat May 10 09:46:41 2025: Line contains 'error'",
    "Sat May 10 09:46:41 2025: 'info'",
    "Sat May 10 09:46:42 2025: 'warn'"
  ]
}
```

## Troubleshooting:

* **File Not Found Error**: Ensure the files are correctly placed in the `unprocessed` folder.
* **No Files to Process**: The system will wait if no files are available in the `unprocessed` folder.
* **Trace/Errors Not Updating**: Ensure that the `--trace` flag is enabled to track traces and errors.


