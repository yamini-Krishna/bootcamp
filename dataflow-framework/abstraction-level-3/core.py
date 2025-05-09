from typing import List, Callable

ProcessorFn = Callable[[str], str]

def process_lines(lines: List[str], processors: List[ProcessorFn]) -> List[str]:
    for processor in processors:
        lines = [processor(line) for line in lines]
    return lines
