cores = [
    '\033[m',    # 0 - Reset
    '\033[3m',   # 1 - Itálico
    '\033[31m',  # 2 - Vermelho
    '\033[34m'   # 3 - Azul
]


def title(txt, cor=0):
    tam = len(txt) + 4

    print(cores[cor], end='')
    print('=' * tam)
    print(f'  {txt}')
    print('=' * tam, end='')
    print(cores[0])
