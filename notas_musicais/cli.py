from rich import print
from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from notas_musicais.acordes import acorde as _acorde
from notas_musicais.escalas import escala as _escala

app = Typer()


@app.command()
def escala(
    tonica: str = Argument('C', help='Tônica da escala'),
    tonalidade: str = Argument('maior', help='Tonalidade da escala'),
):
    console = Console()
    table = Table()
    notas, graus = _escala(tonica, tonalidade).values()
    for grau in graus:
        table.add_column(grau)
    table.add_row(*notas)
    console.print(table)


@app.command()
def acorde(
    cifra: str = Argument('C', help='Cifra de um acorde'),
):
    console = Console()
    table = Table()
    notas_acorde, graus_acorde = _acorde(cifra).values()
    for grau in graus_acorde:
        table.add_column(grau)
    table.add_row(*notas_acorde)
    console.print(table)
