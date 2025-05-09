from cli import get_app
from pipeline import load_pipeline
from core import process_lines

def run_pipeline(input_path: str, output_path: str, config_path: str):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    processors = load_pipeline(config_path)
    processed = process_lines(lines, processors)

    with open(output_path, 'w') as f:
        for line in processed:
            f.write(line)

app = get_app(run_pipeline)

if __name__ == "__main__":
    app()
