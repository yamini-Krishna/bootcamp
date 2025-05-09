# processors/start.py

from typing import Iterator, Tuple

# processors/start.py
class TagLines:
    def process(self, lines: Iterator[Tuple[str, str]]) -> Iterator[Tuple[str, str]]:
        for line in lines:
            print(f"Processing line: {line}")  # Add print to track flow
            if "ERROR" in line:
                yield "error", line
            elif "WARNING" in line:
                yield "warn", line
            else:
                yield "general", line
