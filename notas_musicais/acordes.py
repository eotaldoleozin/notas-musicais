from notas_musicais.escalas import NOTAS, escala


def _menor(cifra):
    nota, _ = cifra.split('m')
    notas_acorde = triade(nota, 'menor')
    if '+' in cifra:
        notas_acorde[2] = semitom(notas_acorde[2], 1)
        graus_acorde = ['I', 'III-', 'V+']
    else:
        graus_acorde = ['I', 'III-', 'V']
    return notas_acorde, graus_acorde


def semitom(nota: str, intervalo: int) -> str:
    index_nota = NOTAS.index(nota)
    index_nota_corrigida = (index_nota + intervalo) % 12
    nota_corrigida = NOTAS[index_nota_corrigida]
    return nota_corrigida


def triade(nota: str, tonalidade: str) -> list[str]:
    graus = [0, 2, 4]
    notas = escala(nota, tonalidade)['notas']
    notas_acorde = []
    for grau in graus:
        notas_acorde.append(notas[grau])
    return notas_acorde


def acorde(cifra: str) -> dict[str, list[str]]:
    """
    Gera as notas de um acorde partindo de uma crifra.
    Parameters:
        cifra: Um acorde em forma de cifra.
    Returns:
        Um diconário com as notas e o graus correspondentes a escala maior.
    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}

        >>> acorde('Cm')
        {'notas': ['C', 'D#', 'G'], 'graus': ['I', 'III-', 'V']}

        >>> acorde('C°')
        {'notas': ['C', 'D#', 'F#'], 'graus': ['I', 'III-', 'V-']}

        >>> acorde('C+')
        {'notas': ['C', 'E', 'G#'], 'graus': ['I', 'III', 'V+']}

        >>> acorde('Cm+')
        {'notas': ['C', 'D#', 'G#'], 'graus': ['I', 'III-', 'V+']}
    """
    if 'm' in cifra:
        notas_acorde, graus_acorde = _menor(cifra)
    elif '°' in cifra:
        nota, _ = cifra.split('°')
        notas_acorde = triade(nota, 'menor')
        notas_acorde[2] = semitom(notas_acorde[2], -1)
        graus_acorde = ['I', 'III-', 'V-']
    elif '+' in cifra:
        nota, _ = cifra.split('+')
        notas_acorde = triade(nota, 'maior')
        notas_acorde[2] = semitom(notas_acorde[2], 1)
        graus_acorde = ['I', 'III', 'V+']
    else:
        nota = cifra
        notas_acorde = triade(nota, 'maior')
        graus_acorde = ['I', 'III', 'V']

    return {'notas': notas_acorde, 'graus': graus_acorde}
