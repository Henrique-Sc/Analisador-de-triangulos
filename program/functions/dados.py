from PIL import Image
from format import formatacao
from time import sleep


def leiaInt(msg=''):
    while True:
        try:
            num = int(input(msg).strip())
        except (ValueError, TypeError):
            print(f'{formatacao[2]}ERRO! Digite um valor válido.{formatacao[0]}')
            sleep(0.5)
        else:
            return num


# def receberTriang(msg):
#
#     while True:
#         quantTriang = leiaInt(msg)
#         if quantTriang <= 0:
#             print(f'{formatacao[2]}Digite um valor maior ou igual a 1.')
#

    # if quantTriang <= 0:
    #     print(f'\nDeseja realmente analisar \"{quantTriang}\" triângulos? isso fará com que o programa não execute a '
    #           f'análise.')
    #     quantTriang = int(input('Quantos triângulos deseja analizar? ').strip())
    #     return quantTriang


def escolha(txt):
    esc = input(txt).strip().upper()[0]

    if esc not in 'SN':
        print()
    while esc not in 'SN':
        esc = input('Valor inválido! Digite S [Sim] ou N [Não]: ').strip().upper()[0]

    if esc == "S":
        return True
    else:
        return False


print(f"O número digitado foi: {leiaInt('Digite um número inteiro: ')}")
