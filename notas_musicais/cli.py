from rich import print
from rich.console import Console
from rich.table import Table
from typer import Argument, Typer

from notas_musicais.acordes import acorde as _acorde
from notas_musicais.campo_harmonico import campo_harmonico as _campo_harmonico
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


@app.command()
def campo_harmonico(
    tonica: str = Argument('C', help='Tônica do Campo Harmônico'),
    tonalidade: str = Argument('maior', help='Tonalidade do campor harmônico'),
):
    console = Console()
    table = Table()
    acordes_campo_harmonico, graus_campo_harmonico = _campo_harmonico(
        tonica, tonalidade
    ).values()
    for grau in graus_campo_harmonico:
        table.add_column(grau)
    table.add_row(*acordes_campo_harmonico)
    console.print(table)
