from engine import run_dag
from config import CONFIG

def main():
    input_lines = [
        "  ERROR: something failed",
        "WARNING: check this setting",
        "INFO: all good"
    ]
    run_dag(CONFIG, "trim", input_lines)  # Starts the DAG from 'trim' node

if __name__ == "__main__":
    main()
