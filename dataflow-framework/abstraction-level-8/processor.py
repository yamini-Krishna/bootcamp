import time
from utils import trace_log, record_metrics, log_error

def process_line(line, trace_enabled):
    time.sleep(0.1)
    if "error" in line:
        raise ValueError("Line contains 'error'")
    label = "info" if "info" in line else "warn"
    return label

def process_file(file_path, trace_enabled):
    print(f"Processing {file_path}...")  # Debugging line
    # Your processing code here

    # Fixed line: Use file_path instead of path
    with open(file_path) as f:
        for line in f:
            start = time.time()
            try:
                label = process_line(line.strip(), trace_enabled)
                if trace_enabled:
                    trace_log(label)
                record_metrics(label, time.time() - start)
            except Exception as e:
                log_error(str(e))
