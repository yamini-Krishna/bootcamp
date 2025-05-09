
import typer
from main import process
from dotenv import load_dotenv

app = typer.Typer()

# Load .env file
load_dotenv()

@app.command()
def run(
    input: str = typer.Option(..., "--input", help="Input file path"),
    output: str = typer.Option(None, "--output", help="Output file path"),
    mode: str = typer.Option("uppercase", "--mode", help="Processing mode"),
):
    """
    Command to process the input file and generate the output
    """
    process(input, output, mode)

if __name__ == "__main__":
    app()
