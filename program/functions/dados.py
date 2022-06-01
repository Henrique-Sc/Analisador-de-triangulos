def leiaInt(t=''):
    while True:
        txt = input(t)

        if txt.strip().isnumeric():
            num = int(txt)
            break
        else:
            print('\033[31mValor inválido! Digite um número inteiro.\033[m')

    return num
