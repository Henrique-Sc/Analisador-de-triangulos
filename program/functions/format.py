formatacao = [
    '\033[m',         # 0 - Reset
    '\033[1m',        # 1 - Negrito
    '\033[3m',        # 2 - Itálico
    '\033[38;5;9m',   # 3 - Vermelho
    '\033[38;5;10m',  # 4 - Verde
    '\033[38;5;11m',  # 5 - Amarelo
    '\033[38;5;12m',  # 6 - Azul
    '\033[38;5;13m',  # 7 - Magenta
    '\033[38;5;14m',  # 8 - Ciano
    '\033[38;5;15m'   # 9 - Branco
]


def title(txt, cor=0):
    txt = txt.strip()
    tam = len(txt) + 4

    print(formatacao[cor], end='')
    print('=' * tam)
    print(f'  {txt}')
    print('=' * tam, end='')
    print(formatacao[0])
