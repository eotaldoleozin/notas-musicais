from notas_musicais.acordes import acorde
from notas_musicais.escalas import escala


def _triade_na_escala(nota: str, notas_da_escala: list[str]) -> str:
    """
    Saber se as notas de um acorde estão na escala.

    Examples:
        >>> _triade_na_escala('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'C'
        >>> _triade_na_escala('D', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'Dm'
        >>> _triade_na_escala('B', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
        'B°'
    """
    tonica, terca, quinta = acorde(nota)['notas']

    match terca in notas_da_escala, quinta in notas_da_escala:
        case True, True:
            return tonica
        case False, True:
            return f'{tonica}m'
        case False, False:
            return f'{tonica}°'


def campo_harmonico(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera um campo harmônico com base em uma tônica e uma tonalidade.
    Parameters:
        tonica: Primeiro grau do campo harmônico.
        tonalidade: tonalidade do campo. Ex: maior, menor, etc...
    Returns:
        Um dicionário com os acordes do campo harmônico e seus respectivos graus.
    Examples:
        >>> campo_harmonico('C', 'maior')
        {'acordes': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'B°'], 'graus': ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']}
    """
    notas, graus = escala(tonica, tonalidade).values()

    acordes_campo_harmonico = []
    graus_campo_harmonico = []

    for nota, grau in zip(notas, graus):
        acorde = _triade_na_escala(nota, notas)
        acordes_campo_harmonico.append(acorde)
        if '°' in acorde:
            grau = f'{grau.lower()}°'
        elif 'm' in acorde:
            grau = f'{grau.lower()}'
        graus_campo_harmonico.append(grau)

    return {'acordes': acordes_campo_harmonico, 'graus': graus_campo_harmonico}
