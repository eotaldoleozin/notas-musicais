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
    'tonica, tonalidade, esperado',
    [
        ('C', 'maior', 'C D E F G A B'.split()),
        ('C#', 'maior', 'C# D# F F# G# A# C'.split()),
        ('D', 'maior', 'D E F# G A B C#'.split()),
        ('D#', 'maior', 'D# F G G# A# C D'.split()),
        ('E', 'maior', 'E F# G# A B C# D#'.split()),
        ('F', 'maior', 'F G A A# C D E'.split()),
        ('F#', 'maior', 'F# G# A# B C# D# F'.split()),
        ('G', 'maior', 'G A B C D E F#'.split()),
        ('G#', 'maior', 'G# A# C C# D# F G'.split()),
        ('A', 'maior', 'A B C# D E F# G#'.split()),
        ('A#', 'maior', 'A# C D D# F G A'.split()),
        ('B', 'maior', 'B C# D# E F# G# A#'.split()),
        ('C', 'menor', 'C D D# F G G# A#'.split()),
        ('C#', 'menor', 'C# D# E F# G# A B'.split()),
        ('D', 'menor', 'D E F G A A# C'.split()),
        ('D#', 'menor', 'D# F F# G# A# B C#'.split()),
        ('E', 'menor', 'E F# G A B C D'.split()),
        ('F', 'menor', 'F G G# A# C C# D#'.split()),
        ('F#', 'menor', 'F# G# A B C# D E'.split()),
        ('G', 'menor', 'G A A# C D D# F'.split()),
        ('G#', 'menor', 'G# A# B C# D# E F#'.split()),
        ('A', 'menor', 'A B C D E F G'.split()),
        ('A#', 'menor', 'A# C C# D# F F# G#'.split()),
        ('B', 'menor', 'B C# D E F# G A'.split()),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):
    resultado = escala(tonica, tonalidade)
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    resultado = escala('c', 'maior')
    assert esperado == resultado['graus']
