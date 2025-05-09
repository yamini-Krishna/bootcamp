def trim_processor():
    def inner(lines):
        for line in lines:
            yield ("trimmed", line.strip())
    return inner

def tag_error_processor():
    def inner(lines):
        for tag, line in lines:
            if "ERROR" in line:
                yield ("errors", line)
            else:
                yield ("pass", line)
    return inner

def tag_warn_processor():
    def inner(lines):
        for tag, line in lines:
            if "WARNING" in line:
                yield ("warnings", line)
            else:
                yield ("pass", line)
    return inner

def print_processor():
    def inner(lines):
        for tag, line in lines:
            print(f"PRINT: {line}")
            yield ("out", line)
    return inner

def archive_processor():
    def inner(lines):
        for tag, line in lines:
            print(f"ARCHIVED: {line}")
            yield ("out", line)
    return inner

def count_processor():
    def inner(lines):
        count = 0
        for tag, line in lines:
            count += 1
        print(f"COUNT: {count}")
        yield ("out", str(count))
    return inner
