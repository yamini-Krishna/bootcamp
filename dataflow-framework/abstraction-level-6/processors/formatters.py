# processors/formatters.py

from typing import Iterator, Tuple

class SnakeCase:
    def process(self, lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
        """
        Formats lines to snake_case (just an example, can be any format)
        :param lines: The input lines to process
        :yield: Tuples of (tag, formatted line)
        """
        for tag, line in lines:
            formatted_line = line.replace(" ", "_").lower()
            yield tag, formatted_line
