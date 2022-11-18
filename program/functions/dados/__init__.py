from ..format import *


def erro(msg=''):
    print(f'{formatacao[3]}ERRO! {msg}{formatacao[0]}')
    sleep(1)


def userInterrupt():
    erro('O usuário encerrou o programa.')


def leiaInt(msg=''):
    while True:
        try:
            num = int(input(msg).strip())
        except (ValueError, TypeError):
            erro('Digite um valor válido.')
        else:
            return num


def leiaFloat(msg=''):
    while True:
        try:
            num = float(input(msg).strip())
        except (ValueError, TypeError):
            erro('Digite um valor válido')
        else:
            return num


def quantTriang(msg):
    try:
        while True:
            quant_Triang = leiaInt(msg)
            if quant_Triang <= 0:
                erro('Digite um valor maior ou igual a 1.')
            else:
                return quant_Triang

    except KeyboardInterrupt:
        userInterrupt()
        return False


def escolha():
    while True:
        try:
            esc = input(f'Digita [{formatacao[6]}S{formatacao[0]}] para Sim '
                        f'ou [{formatacao[3]}N{formatacao[0]}] para Não: ').strip().upper()[0]
            if esc not in 'SN':
                erro('Valor inválido.')
            else:
                print(f'{formatacao[2]}Valor recebido: {formatacao[1]}\"N\"{formatacao[0]}')
                if esc == 'S':
                    return True
                else:
                    return False

        except IndexError:
            erro('Valor inválido.')


def dadosTriang(quant_Triangs):
    dados_Triangs = list()
    for c in range(quant_Triangs):
        # Título - saber qual é o triângulo
        print()
        title(f'{c + 1}º triângulo', cor=3)
        sleep(1.5)

        print(f'\nDigite as informações:')
        sleep(1)

        # Digitar as informações (medidas) do triângulo:
        temp = (leiaFloat('Lado A: '), leiaFloat('Lado B: '), leiaFloat('Lado C: '))
        dados_Triangs.append(temp[:])
        del temp  #  apagar a variável temp após salvar os dados na lista dados_Triangs

        sleep(1.5)

    # Retornar uma lista, onde cada indice vai conter uma tupla com as medidas do triângulo
    return dados_Triangs
