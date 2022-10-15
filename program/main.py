from math import sqrt, degrees
from numpy import arccos
from PIL import Image
from time import sleep
from functions import format, dados

while True:
    try:
        # Resumo sobre o programa
        format.title('Analizador de triângulos', cor=3)
        sleep(1)

        print(f'''
{format.formatacao[2]}Com base no comprimento dos triângulos informados, retorna dados, como: 
    > tipo de triângulo
    > área
    > perímetro
    > ângulos
    > Equivalência entre os triângulos informados.{format.formatacao[0]}''')
        sleep(1)

        # Perguntar ao usuário quantos triângulos ele quer analizar
        while True:
            quantTriang = dados.leiaInt('\nQuantos triângulos deseja analizar? ')
            if quantTriang <= 0:
                dados.erro('Digite um valor maior ou igual a 1.')
            else:
                break

        # Linha amarela
        format.flinha(cor=5)

        # Fazer uma opção para ver uma imagem de exemplo para visualizar as informações
        print(f'\nDeseja visualizar uma {format.formatacao[6]}imagem de exemplo{format.formatacao[0]} para facilitar a inserção e leitura dos dados?\n')
        sleep(3)
        if dados.escolha():
            Image.open('images/triangle.png').show()

        # Linha amarela
        format.flinha(cor=5)

        # Inserir os dados do(s) triângulo(s)
        triangs = dados.dadosTriang(quantTriang)

        # Linha amarela
        format.flinha(cor=5)

        # for c in range(0, quant_triang):
        #     sleep(0.5)
        #
        #     # Título
        #     print()
        #     print('=' * 37)
        #     print(f'\n{f" {c + 1}º Triângulo ":-^37}')
        #
        #     # Entrada dos dados
        #     print('\nDigite as informações: ')
        #     print()
        #     temp.append(float(input('Lado A: ').strip()))
        #     temp.append(float(input('Lado B: ').strip()))
        #     temp.append(float(input('Lado C: ').strip()))
        #
        #     # Inserindo os dados e limpando a lista temp
        #     triangs.append(temp[:])
        #     temp.clear()
        #
        #     print()
        #     print('=' * 37)
        #
        # sleep(0.5)
        # print('\n\n=-=-=-=-= Análise dos dados =-=-=-=-=\n')
        #
        # # Resultado
        # for i, triang in enumerate(triangs):
        #     sleep(1.5)
        #     print()
        #     print('=' * 37)
        #     print(f'\n{f" {i + 1}º Triângulo ":-^37}')
        #     print()
        #
        #     # Criando as variáveis a, b e c para ficar de fácil acesso
        #     a = triang[0]
        #     b = triang[1]
        #     c = triang[2]
        #
        #     # Se com os dados não for possível fazer um triângulo, não realizará os cálculos
        #     if a + b > c and a + c > b and b + c > a:
        #         # Cálculos
        #         s = (a + b + c) / 2  # S - Para realizar a equação de Heron
        #         area = sqrt(s * (s - a) * (s - b) * (s - c))  # Área
        #         peri = a + b + c  # Perímetro
        #
        #         angAB = degrees(arccos((a ** 2 + b ** 2 - c ** 2) / (2 * b * a)))  # Ângulo AB
        #         angBC = degrees(arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))  # Ângulo BC
        #         angAC = degrees(arccos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))  # Ângulo AC
        #
        #         altA = (2 * area) / a  # Altura A
        #         altB = (2 * area) / b  # Altura B
        #         altC = (2 * area) / c  # Altura C
        #
        #         # Saída
        #         if a == b == c:
        #             print('Tipo: Equilátero')
        #         elif a == b or b == c or a == c:
        #             print('Tipo: Isósceles')
        #         else:
        #             print('Tipo: Escaleno')
        #
        #         print(f'\nÁrea: {area:.2f} | Perímetro: {peri:.2f}')
        #         print(f'ângulo AB: {angAB:.2f}° | ângulo BC: {angBC:.2f}° | ângulo AC: {angAC:.2f}°')
        #         print(f'Altura A: {altA:.2f} | Altura B: {altB:.2f} | Altura C: {altC:.2f}')
        #
        #     else:
        #         print('Com esses dados, não é possível fazer um triângulo!')
        #     print()
        #     print('=' * 37)
        #     print()
        sleep(1.5)

        print('\nFim da execução. Volte sempre (•◡•)/')

        break

    except KeyboardInterrupt:
        print('')
        dados.userInterrupt()
        sleep(1)
        print('')
        format.title('O programa será reiniciado...', 5)
        sleep(2)
        print('')
