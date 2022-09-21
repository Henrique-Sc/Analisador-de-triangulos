from PIL import Image
from format import formatacao
from time import sleep


def erro(msg=''):
    print(f'{formatacao[3]}ERRO! {msg}{formatacao[0]}')


def userInterrupt():
    erro('O usuário encerrou o programa.')


def leiaInt(msg=''):
    while True:
        try:
            num = int(input(msg).strip())
        except (ValueError, TypeError):
            erro('Digite um valor válido.')
            sleep(0.5)
        else:
            return num


def receberTriang(msg):
    try:
        while True:
            quantTriang = leiaInt(msg)
            if quantTriang <= 0:
                erro('Digite um valor maior ou igual a 1.')
            else:
                return quantTriang
    except KeyboardInterrupt:
        userInterrupt()


def escolha():
    try:
        while True:
            esc = input(f'Digita [{formatacao[6]}S{formatacao[0]}] para Sim '
                        f'ou [{formatacao[3]}N{formatacao[0]}] para Não: ').strip().upper()[0] 

    except KeyboardInterrupt:
        userInterrupt()
    #
    # if esc not in 'SN':
    #     print()
    # while esc not in 'SN':
    #     erro('Valor inválido! Digite S [Sim] ou N [Não]: ')
    #     esc = input().strip().upper()[0]
    #
    # if esc == "S":
    #     return True
    # else:
    #     return False


escolha()
