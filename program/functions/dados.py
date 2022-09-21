from PIL import Image


def leiaInt(msg=''):
    while True:
        msg_input = input(msg.strip())

        if msg_input.strip().isnumeric():
            num = int(msg_input)
            break
        else:
            print('\033[31mValor inválido! Digite um número inteiro.\033[m')

    return num


def receberTriang(msg):
    quantTriang = leiaInt(msg)

    if quantTriang <= 0:
        print(f'\nDeseja realmente analisar \"{quantTriang}\" triângulos? isso fará com que o programa não execute a '
              f'análise.')
        quantTriang = int(input('Quantos triângulos deseja analizar? ').strip())
        return quantTriang


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
