# yamini_hello/main.py

import typer
from rich import print

app = typer.Typer()

@app.command()
def hello(name: str = "World"):
    print(f"[bold green]Hello, {name}![/bold green]")

if __name__ == "__main__":
    app()
