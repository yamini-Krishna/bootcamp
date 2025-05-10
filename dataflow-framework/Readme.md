
# Real-Time File Processing System

This project implements a dynamic, observable, fault-tolerant, and self-managing file processing system that supports both single-file processing and continuous monitoring.

## Features
- **Single File Mode**: Processes one file and exits.
- **Watch Mode**: Continuously monitors a directory and processes files as they appear.
- **Web Dashboard**: Accessible endpoints to view system health, statistics, and processed files.
- **Docker Support**: Build and run the project in a containerized environment.

## Installation

### Prerequisites

- Python 3.7+
- Docker (for containerized runs)

### Steps

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

To run the file processing system locally in **Single File Mode**:

```bash
python main.py --input somefile.txt
````

To run in **Watch Mode** (continuously monitoring the `watch_dir/unprocessed/` folder):

```bash
python main.py --watch
```

### Docker Support

1. **Build the Docker image**:

   ```bash
   make build-docker
   ```

2. **Run the container**:

   ```bash
   make run
   ```

### FastAPI Endpoints

* `/stats`: View system statistics (e.g., processed files count, errors).
* `/health`: Check if the system is running and healthy.
* `/files`: Retrieve the list of processed files.

### File Upload

* **Upload files** via FastAPI's file upload feature or use `rsync` to upload files to the `watch_dir/unprocessed/` folder.

### Monitoring Uptime

To monitor the uptime of your deployed system, consider using a free service like [Better Uptime](https://betteruptime.com/).

## Commands in Makefile

* `make build-docker`: Builds the Docker image.
* `make run`: Runs the project in a container.
* `make build-package`: Packages the project for distribution.
* `make publish-package`: Publishes the package to a registry.
* `make clean`: Cleans up generated files.

## Notes

* Ensure the folder `watch_dir/unprocessed/` exists and has appropriate permissions for file uploads.
* You can customize the `watch_dir` in the configuration if needed.


