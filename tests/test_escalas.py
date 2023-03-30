from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    tonica = 'c'
    tonalidade = 'maior'

    result = escala(tonica, tonalidade)

    assert result


def test_deve_retornar_uma_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'x'
    tonalidade = 'maior'

    mensagem = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert error.value.args[0] == mensagem


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem = f'Essa escala não existe ou não foi implementada. Tente uma dessas: {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert error.value.args[0] == mensagem


@mark.parametrize(
    'tonica, esperado',
    [
        ('C', 'C D E F G A B'.split()),
        ('C#', 'C# D# F F# G# A# C'.split()),
        ('D', 'D E F# G A B C#'.split()),
        ('D#', 'D# F G G# A# C D'.split()),
        ('E', 'E F# G# A B C# D#'.split()),
        ('F', 'F G A A# C D E'.split()),
        ('F#', 'F# G# A# B C# D# F'.split()),
        ('G', 'G A B C D E F#'.split()),
        ('G#', 'G# A# C C# D# F G'.split()),
        ('A', 'A B C# D E F# G#'.split()),
        ('A#', 'A# C D D# F G A'.split()),
        ('B', 'B C# D# E F# G# A#'.split()),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    resultado = escala('c', 'maior')
    assert esperado == resultado['graus']
