from pytest import mark

from notas_musicais.acordes import acorde


@mark.parametrize(
    'cifra, esperado',
    [
        ('C', 'C E G'.split()),
        ('C#', 'C# F G#'.split()),
        ('D', 'D F# A'.split()),
        ('D#', 'D# G A#'.split()),
        ('E', 'E G# B'.split()),
        ('F', 'F A C'.split()),
        ('F#', 'F# A# C#'.split()),
        ('G', 'G B D'.split()),
        ('G#', 'G# C D#'.split()),
        ('A', 'A C# E'.split()),
        ('A#', 'A# D F'.split()),
        ('B', 'B D# F#'.split()),
        ('Cm', 'C D# G'.split()),
        ('C#m', 'C# E G#'.split()),
        ('Dm', 'D F A'.split()),
        ('D#m', 'D# F# A#'.split()),
        ('Em', 'E G B'.split()),
        ('Fm', 'F G# C'.split()),
        ('F#m', 'F# A C#'.split()),
        ('Gm', 'G A# D'.split()),
        ('G#m', 'G# B D#'.split()),
        ('Am', 'A C E'.split()),
        ('A#m', 'A# C# F'.split()),
        ('Bm', 'B D F#'.split()),
        ('C°', 'C D# F#'.split()),
        ('C#°', 'C# E G'.split()),
        ('D°', 'D F G#'.split()),
        ('D#°', 'D# F# A'.split()),
        ('E°', 'E G A#'.split()),
        ('F°', 'F G# B'.split()),
        ('F#°', 'F# A C'.split()),
        ('G°', 'G A# C#'.split()),
        ('G#°', 'G# B D'.split()),
        ('A°', 'A C D#'.split()),
        ('A#°', 'A# C# E'.split()),
        ('B°', 'B D F'.split()),
        ('C+', 'C E G#'.split()),
        ('C#+', 'C# F A'.split()),
        ('D+', 'D F# A#'.split()),
        ('D#+', 'D# G B'.split()),
        ('E+', 'E G# C'.split()),
        ('F+', 'F A C#'.split()),
        ('F#+', 'F# A# D'.split()),
        ('G+', 'G B D#'.split()),
        ('G#+', 'G# C E'.split()),
        ('A+', 'A C# F'.split()),
        ('A#+', 'A# D F#'.split()),
        ('B+', 'B D# G'.split()),
        ('Cm+', 'C D# G#'.split()),
        ('C#m+', 'C# E A'.split()),
        ('Dm+', 'D F A#'.split()),
        ('D#m+', 'D# F# B'.split()),
        ('Em+', 'E G C'.split()),
        ('Fm+', 'F G# C#'.split()),
        ('F#m+', 'F# A D'.split()),
        ('Gm+', 'G A# D#'.split()),
        ('G#m+', 'G# B E'.split()),
        ('Am+', 'A C F'.split()),
        ('A#m+', 'A# C# F#'.split()),
        ('Bm+', 'B D G'.split()),
    ],
)
def test_acorde_deve_retornar_as_notas_correspondentes(cifra, esperado):
    notas, _ = acorde(cifra).values()
    assert notas == esperado


@mark.parametrize(
    'cifra, esperado',
    [
        ('C', 'I III V'.split()),
        ('Cm', 'I III- V'.split()),
        ('C°', 'I III- V-'.split()),
        ('C+', 'I III V+'.split()),
        ('Cm+', 'I III- V+'.split()),
    ],
)
def test_acorde_deve_retornar_os_graus_correspondentes(cifra, esperado):

    _, graus = acorde(cifra).values()
    assert graus == esperado
