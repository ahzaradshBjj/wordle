import typer

app = typer.Typer()

@app.command()
def get_input(confirmacion: str):
    confirmacion = confirmacion.lower().strip()
    if confirmacion == 'y' or confirmacion == 'yes':
        entrada = input("Ingresa palabra: ")


if __name__ == '__main__':
    app()