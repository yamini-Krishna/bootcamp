def process_line(line, metrics):
    # Example logic for processing different types of lines
    if line.startswith("error"):
        metrics.update_line_count('error')
        metrics.update_error_count()
        metrics.add_trace(["start", "error", "end"])
    elif line.startswith("warn"):
        metrics.update_line_count('warn')
        metrics.add_trace(["start", "warn", "end"])
    else:
        metrics.update_line_count('general')
        metrics.add_trace(["start", "general", "end"])

def process_lines(lines, metrics):
    for line in lines:
        process_line(line, metrics)
