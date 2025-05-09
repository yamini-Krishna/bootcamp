
from typing import Optional, Iterator
from pipeline import get_pipeline
from core import to_uppercase, to_snakecase
import os

def read_lines(path: str) -> Iterator[str]:
    """
    Reads the lines from the input file.
    """
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

def write_output(lines: Iterator[str], output_path: Optional[str]):
    """
    Writes the processed lines to the output file or prints to console.
    """
    if output_path:
        with open(output_path, "w") as f:
            for line in lines:
                f.write(line + "\n")
    else:
        for line in lines:
            print(line)

def process(input: str, output: Optional[str], mode: str):
    """
    Main function to process the input file and write to output.
    """
    lines = read_lines(input)
    pipeline = get_pipeline(mode)  # Get the appropriate pipeline based on the mode
    for line in lines:
        for processor in pipeline:
            line = processor(line)  # Apply each processor in the pipeline
        write_output([line], output)
