from time import sleep

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
]


def title(txt, cor=0, tam=30):

    if tam == 0:
        tam = len(txt) + 4

    print(formatacao[cor], end='')
    print('=' * tam)
    print(f'{txt}'.center(tam))
    print('=' * tam, end='')
    print(formatacao[0])


def subtile(txt, cor=0):
    print(f'{formatacao[cor]}-={formatacao[0]}' * 4, txt, f'{formatacao[cor]}=-{formatacao[0]}' * 4)


def linha(tmn=30, simb='=', cor=0):
    print(f'{formatacao[cor]}{simb}{formatacao[0]}' * tmn)


def flinha(tmn=30, simb='=', cor=0, time=1, quebra=True):
    if quebra: print()
    sleep(time)
    linha(tmn=tmn, simb=simb, cor=cor)
    sleep(time)
