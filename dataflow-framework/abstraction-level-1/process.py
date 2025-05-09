import typer
from typing import Optional, Iterator
from dotenv import load_dotenv
import os

app = typer.Typer()

# Load .env file
load_dotenv()
DEFAULT_MODE = os.getenv("MODE", "uppercase")

if DEFAULT_MODE is None:
    print("Warning: 'MODE' not found in .env, defaulting to 'uppercase'.")


def read_lines(path: str) -> Iterator[str]:
    try:
        with open(path, "r") as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        raise
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{path}'.")
        raise


def transform_line(line: str, mode: str) -> str:
    if mode == "snakecase":
        return line.replace(" ", "_").lower()
    else:  # Default to uppercase
        return line.upper()


def write_output(lines: Iterator[str], output_path: Optional[str]):
    if output_path:
        try:
            with open(output_path, "w") as f:
                for line in lines:
                    f.write(line + "\n")
        except PermissionError:
            print(f"Error: You don't have permission to write to the file '{output_path}'.")
    else:
        for line in lines:
            print(line)


@app.command()
def process(
    input: str = typer.Option(..., "--input", help="Input file path"),
    output: Optional[str] = typer.Option(None, "--output", help="Output file path"),
    mode: str = typer.Option(DEFAULT_MODE, "--mode", help="Processing mode"),
):
    lines = read_lines(input)
    transformed = (transform_line(line, mode) for line in lines)
    write_output(transformed, output)


if __name__ == "__main__":
    app()
