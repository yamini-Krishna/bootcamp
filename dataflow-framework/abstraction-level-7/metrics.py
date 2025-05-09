# metrics.py
class Metrics:
    def __init__(self):
        self.total_lines_processed = 0
        self.total_processing_time = 0.0
        self.total_errors = 0
        self.lines_processed_by_each_processor = {}
        self.recent_traces = []
        self.recent_errors = []

    def update_processor_count(self, processor_name):
        self.total_lines_processed += 1
        if processor_name not in self.lines_processed_by_each_processor:
            self.lines_processed_by_each_processor[processor_name] = 0
        self.lines_processed_by_each_processor[processor_name] += 1

    def update_processing_time(self, processing_time):
        self.total_processing_time += processing_time

    def update_error_count(self):
        self.total_errors += 1
        # Add to recent errors for tracking
        self.recent_errors.append("An error occurred")

    def add_trace(self, trace):
        # Keep track of recent traces (e.g., processor names)
        if len(self.recent_traces) >= 100:  # Limit trace history to 100 items
            self.recent_traces.pop(0)
        self.recent_traces.append(trace)
