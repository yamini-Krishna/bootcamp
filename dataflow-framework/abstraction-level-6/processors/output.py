# processors/output.py

from typing import Iterator, Tuple

# processors/output.py
class Terminal:
    def process(self, lines: Iterator[Tuple[str, str]]) -> Iterator[Tuple[str, str]]:
        for tag, line in lines:
            print(f"Output: {line}")  # Print output to terminal

