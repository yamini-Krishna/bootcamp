from collections import defaultdict, deque
import time

metrics = {
    "total_lines_processed": 0,
    "total_processing_time": 0.0,
    "total_errors": 0,
    "lines_processed_by_each_processor": {},
    "current_file": None,
    "last_processed": [],
    "trace": [],
    "errors": []
}


def record_metrics(label, duration):
    metrics["total_lines_processed"] += 1
    metrics["total_processing_time"] += duration
    metrics["lines_processed_by_each_processor"][label] += 1

def trace_log(label):
    metrics["trace"].append(label)

def log_error(msg):
    metrics["total_errors"] += 1
    metrics["errors"].append(f"{time.ctime()}: {msg}")
