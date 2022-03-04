from math import sqrt, degrees
from numpy import arccos
from PIL import Image
from time import sleep

reset = '\033[m'
italico = '\033[3m'

# Resumo sobre o programa
print('===== Analizador de triângulos =====')

print(f'''
{italico}Com base no comprimento dos triângulos informados, retorna dados, como: 
    > tipo de triângulo
    > área
    > perímetro
    > ângulos
    > Equivalência entre os triângulos informados.{reset}''')

# Perguntar ao usuário quantos triângulos ele quer analizar
quant_triang = int(input('\nQuantos triângulos deseja analizar? ').strip())

# Se o usúario digitar 0, mostrará uma mensagem se ele quer mesmo continuar (Assim, o programa iria fechar)
if quant_triang == 0:
    print('\nDeseja realmente analisar 0 triângulos? isso fará com que o programa não execute a análise.')
    quant_triang = int(input('Quantos triângulos deseja analizar? ').strip())

sleep(0.5)

if quant_triang >= 1:
    # Declaração das variáveis
    triangs = []
    temp = []

    # Fazer uma opção para ver uma imagem de exemplo para visualizar as informações
    esc = input('\nDeseja visualizar uma imagem de exemplo para facilitar a inserção e leitura dos dados? S [Sim] ou N [Não]: ').strip().upper()[0]

    if esc not in 'SN': print()
    while esc not in 'SN':
        esc = input('Valor inválido! Digite S [Sim] ou N [Não]: ').strip().upper()[0]

    if esc == 'S':
        Image.open('imagens/triangulo.png').show()

    # Laço para inserir os dados sobre os triângulos
    for c in range(0, quant_triang):
        sleep(0.5)

        # Título
        print()
        print('=' * 37)
        print(f'\n{f" {c + 1}º Triângulo ":-^37}')

        # Entrada dos dados
        print('\nDigite as informações: ')
        print()
        temp.append(float(input('Lado A: ').strip()))
        temp.append(float(input('Lado B: ').strip()))
        temp.append(float(input('Lado C: ').strip()))

        # Inserindo os dados e limpando a lista temp
        triangs.append(temp[:])
        temp.clear()

        print()
        print('=' * 37)

    sleep(0.5)
    print('\n\n=-=-=-=-= Análise dos dados =-=-=-=-=\n')


    # Resultado
    for i, triang in enumerate(triangs):
        sleep(1.5)
        print()
        print('=' * 37)
        print(f'\n{f" {i + 1}º Triângulo ":-^37}')
        print()

        # Criando as variáveis a, b e c para ficar de fácil acesso
        a = triang[0]
        b = triang[1]
        c = triang[2]

        # Se com os dados não for possível fazer um triângulo, não realizará os cálculos
        if a + b > c and a + c > b and b + c > a:
            # Cálculos
            s = (a + b + c) / 2  # S - Para realizar a equação de Heron
            area = sqrt(s*(s - a) * (s - b) * (s - c))  # Área
            peri = a + b + c  # Perímetro

            angAB = degrees(arccos((a ** 2 + b ** 2 - c ** 2) / (2 * b * a)))  # Ângulo AB
            angBC = degrees(arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))  # Ângulo BC
            angAC = degrees(arccos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))  # Ângulo AC

            altA = (2 * area) / a  # Altura A
            altB = (2 * area) / b  # Altura B
            altC = (2 * area) / c  # Altura C

            # Saída
            if a == b == c:
                print('Tipo: Equilátero')
            elif a == b or b == c or a == c:
                print('Tipo: Isósceles')
            else:
                print('Tipo: Escaleno')

            print(f'\nÁrea: {area:.2f} | Perímetro: {peri:.2f}')
            print(f'ângulo AB: {angAB:.2f}° | ângulo BC: {angBC:.2f}° | ângulo AC: {angAC:.2f}°')
            print(f'Altura A: {altA:.2f} | Altura B: {altB:.2f} | Altura C: {altC:.2f}')

        else:
            print('Com esses dados, não é possível fazer um triângulo!')
        print()
        print('=' * 37)
        print()
sleep(1.5)
print('\nFim da execução. Volte sempre \(•◡•)/')