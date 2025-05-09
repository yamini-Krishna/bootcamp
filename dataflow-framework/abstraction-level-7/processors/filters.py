def only_error(line):
    """Filter lines that are errors."""
    if "error" in line:
        print(f"Error line: {line}")
    return line

def only_warn(line):
    """Filter lines that are warnings."""
    if "warn" in line:
        print(f"Warning line: {line}")
    return line
