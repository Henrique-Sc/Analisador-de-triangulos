from ..format import *
from math import sqrt, degrees
from numpy import arccos


def area(a, b, c):
    s = (a + b + c) / 2  # S - Para realizar a equação de Heron
    area = sqrt(s * (s - a) * (s - b) * (s - c))  # Área
    return area


def peri(a, b, c):
    p = a + b + c
    return p


def angulos(a, b, c):
    angAB = degrees(arccos((a ** 2 + b ** 2 - c ** 2) / (2 * b * a)))  # Ângulo AB
    angBC = degrees(arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))  # Ângulo BC
    angAC = degrees(arccos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))  # Ângulo AC

    return angAB, angBC, angAC


def altura(a, b, c, area):
    altA = (2 * area) / a  # Altura A
    altB = (2 * area) / b  # Altura B
    altC = (2 * area) / c  # Altura C

    return altA, altB, altC


def analise(dados_Triangs):
    for i, triang in enumerate(dados_Triangs):
        title(f'{i + 1}º triângulo', cor=3)
        print()
        sleep(1.5)

        # Criando as variáveis a, b e c para ficar de fácil acesso
        ac = triang[0]
        bc = triang[1]
        ab = triang[2]

        print(f'{formatacao[5]}-{formatacao[0]}' * 10, f'Medidas', f'{formatacao[5]}-{formatacao[0]}' * 10)  # ---------- Medidas ----------
        sleep(1)

        print(f'{formatacao[1]}AC:{formatacao[0]} {a}'), sleep(1)
        print(f'{formatacao[1]}BC:{formatacao[0]} {b}'), sleep(1)
        print(f'{formatacao[1]}AB:{formatacao[0]} {c}'), sleep(1)

        linha(simb='-', cor=5, tmn=29)  # Linha amarela

        print()  # Quebra de linha
        sleep(1)
        print(f'{formatacao[5]}-{formatacao[0]}' * 9, f'Resultado', f'{formatacao[5]}-{formatacao[0]}' * 9)  # --------- Resultado ---------
        sleep(1)
        # Verificar se com os dados é possível formar um triângulo
        if a + b > c and a + c > b and b + c > a:  # É possível?
            # calculos
            area_t = area(a, b, c)  # área
            p = peri(a, b, c)  # perímetro
            angs = angulos(a, b, c)  # ângulos
            alts = altura(a, b, c, area_t)  # alturas

            # saída
            print(f'{formatacao[1]}Tipo:{formatacao[0]} {formatacao[0]}', end='')
            if a == b == c:
                print('Equilátero')
            elif a == b or b == c or a == c:
                print('Isósceles')
            else:
                print('Escaleno')
            sleep(1)
            # Área e perímetro

            print(f'\n{formatacao[1]}Área:{formatacao[0]} {area_t:.2f}'), sleep(1)
            print(f'{formatacao[1]}Perímetro:{formatacao[0]} {p:.2f}'), sleep(1)

            # Ângulos
            print(f'\n{formatacao[1]}Ângulo AB:{formatacao[0]} {angs[0]:.2f}°'), sleep(1)
            print(f'{formatacao[1]}Ângulo BC:{formatacao[0]} {angs[1]:.2f}°'), sleep(1)
            print(f'{formatacao[1]}Ângulo AC:{formatacao[0]} {angs[1]:.2f}°'), sleep(1)

            # Alturas
            print(f'\n{formatacao[1]}Altura A:{formatacao[0]} {alts[0]:.2f}'), sleep(1)
            print(f'{formatacao[1]}Altura B:{formatacao[0]} {alts[0]:.2f}'), sleep(1)
            print(f'{formatacao[1]}Altura C:{formatacao[0]} {alts[0]:.2f}')

        else:  # Não é possível...
            print('Com esses dados, não é \npossível formar um triângulo!')
        sleep(1)
        linha(simb='-', cor=5, tmn=29)  # Linha amarela
        print()
        sleep(1.5)

    linha(cor=3)
