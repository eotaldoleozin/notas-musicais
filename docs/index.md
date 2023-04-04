![logo do projeto](assets/logo.png){width="300" .center}
# Notas musicais

Notas musicais é um CLI para ajudar na formação de escalas e acordes.

Possui dois comandos disponíveis: 'escala' e 'acorde'.

## Como usar?

### Escala 

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

#### Mais informações sobre o comando escala

Para obter mais informações sobre o comando escala use a opção --help:

```bash
poetry run notas-musicas escala --help

 Usage: notas-musicais escala [OPTIONS] [TONICA] [TONALIDADE]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica da escala [default: C]                                                        │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### Acorde

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

#### Mais informações sobre o comando acorde

Para obter mais informações sobre o comando acorde use a opção --help:

```bash
poetry run notas-musicais acorde --help

 Usage: notas-musicais acorde [OPTIONS] [CIFRA]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   cifra      [CIFRA]  Cifra de um acorde [default: C]                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```





