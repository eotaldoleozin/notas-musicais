![logo do projeto](assets/logo.png){width="300" .center}
# Notas musicais

## Como usar?

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
poetry run escalas
```

Retornando os graus e as notas correspondentes a essa escala

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir (por default C):

```bash
poetry run escalas G
```

O comando acima retornará a escala maior de tônica Sol:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ G │ A  │ B   │ C  │ D │ E  │ F#  │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alteração da tonalidade da escala

Você pode alterar a tonalidade da escala também! Por padrão a tonalidade é 'maior', porém podemos passar outra
através do segundo parâmetro do CLI:

```bash
poetry run escalas A maior
```

O comando acima retornará a escala maior de Lá:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ A │ B  │ C#  │ D  │ E │ F# │ G#  │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Mais informações sobre o CLI

Para obter mais informações sobre o CLI use a opção --help:

```bash
poetry run escalas --help

Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica da escala [default: C]                                                        │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

