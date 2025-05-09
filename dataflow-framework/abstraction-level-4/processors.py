from typing import Iterator

# Stateless Processor: Uppercase
def simple_processor(lines: Iterator[str]) -> Iterator[str]:
    for line in lines:
        yield line.upper()  # ✅ Now processes one line at a time


# Stateful Processor: Line Counter
class LineCounterProcessor:
    def __init__(self):
        self.count = 0

    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            self.count += 1
            yield f"Line {self.count}: {line}"

# Fan-In Processor: Join every two lines
def join_lines(lines: Iterator[str]) -> Iterator[str]:
    buffer = []
    for line in lines:
        buffer.append(line)
        if len(buffer) == 2:
            yield " ".join(buffer)
            buffer = []
    if buffer:
        yield " ".join(buffer)

# Fan-Out Processor: Split lines by delimiter
def split_lines_by_delimiter(lines: Iterator[str], delimiter: str) -> Iterator[str]:
    for line in lines:
        for sub_line in line.split(delimiter):
            yield sub_line
