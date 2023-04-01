from pytest import mark
from typer.testing import CliRunner

from notas_musicais.cli import app, escalas

runner = CliRunner()


def test_escala_cli_deve_retornar_0_ao_stdout():
    result = runner.invoke(app)
    assert result.exit_code == 0


@mark.parametrize('nota', 'C D E F G A B'.split())
def test_escala_cli_deve_conter_as_notas_na_resposta(nota):
    result = runner.invoke(app)
    assert nota in result.stdout


@mark.parametrize('nota', 'D E F# G A B C#'.split())
def test_escala_cli_deve_conter_as_notas_na_resposta_de_re(nota):
    result = runner.invoke(app, ['D'])
    assert nota in result.stdout


@mark.parametrize('grau', 'I II III IV V VI VII'.split())
def test_escala_cli_deve_conter_todos_os_graus(grau):
    result = runner.invoke(app, ['D'])
    assert grau in result.stdout
