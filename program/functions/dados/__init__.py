from time import sleep
from ..format import *


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


def leiaFloat(msg=''):
    while True:
        try:
            num = float(input(msg).strip())
        except (ValueError, TypeError):
            erro('Digite um valor válido')
            sleep(0.5)
        else:
            return num


def quantTriang(msg):
    try:
        while True:
            quantTriang = leiaInt(msg)
            if quantTriang <= 0:
                erro('Digite um valor maior ou igual a 1.')
            else:
                return quantTriang

    except KeyboardInterrupt:
        userInterrupt()
        quantTriang = 0
        return quantTriang


def escolha():
    while True:
        try:
            esc = input(f'Digita [{formatacao[6]}S{formatacao[0]}] para Sim '
                        f'ou [{formatacao[3]}N{formatacao[0]}] para Não: ').strip().upper()[0]
            if esc not in 'SN':
                erro('Valor inválido.')
            else:
                if esc == 'S':
                    return True
                else:
                    return False

        except IndexError:
            erro('Valor inválido.')


def dadosTriang(quant_triang, cor=0):
    triangs = list()
    temp = list()
    for c in range(quant_triang):
        title(f'{c + 1}º triângulo', cor=cor, tam=26)
        sleep(1)

        print(f'\nDigite as informações:')
        sleep(1)

        temp.append(leiaFloat('Lado A: '))
        temp.append(leiaFloat('Lado B: '))
        temp.append(leiaFloat('Lado C: '))

        triangs.append(temp[:])
        temp.clear()

        print()
        sleep(1)

    return triangs


