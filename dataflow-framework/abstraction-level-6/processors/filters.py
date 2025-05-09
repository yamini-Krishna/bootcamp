# processors/filters.py

from typing import Iterator, Tuple

class OnlyError:
    def process(self, lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
        """
        Only passes through lines tagged 'error'
        :param lines: The input lines to process
        :yield: Tuples of (tag, line) where tag is 'error'
        """
        for tag, line in lines:
            if tag == 'error':
                yield 'error', line

class OnlyWarn:
    def process(self, lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
        """
        Only passes through lines tagged 'warn'
        :param lines: The input lines to process
        :yield: Tuples of (tag, line) where tag is 'warn'
        """
        for tag, line in lines:
            if tag == 'warn':
                yield 'warn', line
