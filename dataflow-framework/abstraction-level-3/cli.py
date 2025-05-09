import typer

def get_app(process_func):
    app = typer.Typer()

    @app.command()
    def main(input: str, output: str, config: str):
        process_func(input, output, config)

    return app
