![logo do projeto](assets/logo.png){width="300" .center}
# Notas musicais

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmônicos.

Toda aplicação é baseada em um comando chamado 'notas-musicais'. Esse comando tem um subomando relacionado
com cada ação que a aplicação pode ralizar, como 'escala', 'acorde' e 'campo-harmonico'.

## Como usar?

### Escalas 

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run notas-musicais escala
```

Como a tônica e a tonalidade são definidas por default como 'C' e 'maior', respectivamente, iremos obter
as notas da escala Dó maior:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir (por default C):

```bash
poetry run notas-musicais escala G
```

O comando acima retornará a escala maior de tônica Sol:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ G │ A  │ B   │ C  │ D │ E  │ F#  │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração da tonalidade da escala

Você pode alterar a tonalidade da escala também! Por padrão a tonalidade é 'maior', porém podemos passar outra
através do segundo parâmetro do CLI:

```bash
poetry run notas-musicais escala A menor
```

O comando acima retornará a escala menor de Lá:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ A │ B  │ C   │ D  │ E │ F  │ G   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Acordes

Uso básico

Podemos verificar as notas que compõem um acorde utilizando o comando abaixo:

```bash
poetry run notas-musicais acorde
```

Por default, a cifra utilizada é Dó maior, de forma que teremos a seguinte resposta:

```
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

#### Variações na cifra

O comando permite que sejam passados como argumento acordes maiores, menores, diminutos, aumentados e 
menores aumentados.

Acorde maior:

```bash
poetry run notas-musicais acorde D

┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ D │ F#  │ A │
└───┴─────┴───┘
```

Acorde menor:

```bash
poetry run notas-musicais acorde Em

┏━━━┳━━━━━━┳━━━┓
┃ I ┃ III- ┃ V ┃
┡━━━╇━━━━━━╇━━━┩
│ E │ G    │ B │
└───┴──────┴───┘
```

Acorde diminuto:

```bash
poetry run notas-musicais acorde F°

┏━━━┳━━━━━━┳━━━━┓
┃ I ┃ III- ┃ V- ┃
┡━━━╇━━━━━━╇━━━━┩
│ F │ G#   │ B  │
└───┴──────┴────┘
```

Acorde aumentado:

```bash
poetry run notas-musicais acorde G+

┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ G │ B   │ D# │
└───┴─────┴────┘
```

Acorde menor aumentado:

```bash
poetry run notas-musicais acorde Am+

┏━━━┳━━━━━━┳━━━━┓
┃ I ┃ III- ┃ V+ ┃
┡━━━╇━━━━━━╇━━━━┩
│ A │ C    │ F  │
└───┴──────┴────┘
```

### Campo harmônico

Você pode chamar os campos harmônicos via o subcomando 'campo-harmonico'. Por exemplo:

```bash
poetry run notas-musicais campo-harmonico

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

Por padrão os argumentos utilizados são a tônica 'C' e a tonalidade 'maior'.

#### Alterações nos campos harmônicos

Você pode alterar a tônica e a tonalidade:

```bash
notas-musicais campo-harmonico [TONICA] [TONALIDADE]
```

Podemos obter o campo harmônico maior de 'Mi' com o seguinte comando:

```bash
poetry run notas-musicais campo-harmonico E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

Podemos obter o campo harmônico menor de 'Sol' com o seguinte comando:

```bash
poetry run notas-musicais campo-harmonico G menor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Gm │ A°  │ A#  │ Cm │ Dm │ D# │ F   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informações sobre o CLI

Podemos obter mais informações sobre o CLI utilizando a flag --help:

```bash
poetry run notas-musicais --help

 Usage: notas-musicais [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell.             │
│                                                              [default: None]                                         │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or  │
│                                                              customize the installation.                             │
│                                                              [default: None]                                         │
│ --help                                                       Show this message and exit.                             │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ acorde                                                                                                               │
│ campo-harmonico                                                                                                      │
│ escala                                                                                                               │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Mais informações sobre os subcomandos

Podemos obter mais informações sobre um subcomando passando a flag --help após o nome desse subcomando.
Por exemplo:

```bash
poetry run notas-musicais escala --help

 Usage: notas-musicais escala [OPTIONS] [TONICA] [TONALIDADE]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica da escala [default: C]                                                        │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```






