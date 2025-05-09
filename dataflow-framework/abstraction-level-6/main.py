# main.py

from engine import run_dag
from config import CONFIG  # Import CONFIG here
from processors.start import TagLines
from processors.filters import OnlyError, OnlyWarn
from processors.formatters import SnakeCase
from processors.output import Terminal

def main():
    # Example input lines
    input_lines = iter([
        "ERROR: Something went wrong",
        "WARNING: Something might go wrong",
        "All good here"
    ])

    # Run the DAG with the configuration and input lines
    run_dag(CONFIG, 'start', input_lines)

if __name__ == '__main__':
    main()
