from ..format import *
from math import sqrt, degrees
from numpy import arccos


def area(a, b, c):
    s = (a + b + c) / 2  # S - Para realizar a equação de Heron
    area_t = sqrt(s * (s - a) * (s - b) * (s - c))  # Área
    return area_t


def peri(a, b, c):
    p = a + b + c
    return p


def angulos(a, b, c):
    ang_a = degrees(arccos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))  # Ângulo A
    ang_b = degrees(arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))  # Ângulo B
    ang_c = degrees(arccos((a ** 2 + b ** 2 - c ** 2) / (2 * b * a)))  # Ângulo C

    return ang_a, ang_b, ang_c


def altura(ac, bc, ab, area_t):
    alt_a = (2 * area_t) / bc  # Altura A
    alt_b = (2 * area_t) / ac  # Altura B
    alt_c = (2 * area_t) / ab  # Altura C

    return alt_a, alt_b, alt_c


def analise(dados_triangs):
    for i, triang in enumerate(dados_triangs):
        title(f'{i + 1}º triângulo', cor=3)
        print()
        sleep(1.5)

        # Criando as variáveis a, b e c para ficar de fácil acesso
        ac = triang[0]
        bc = triang[1]
        ab = triang[2]

        # ---------- Medidas ----------
        print(f'{formatacao[5]}-{formatacao[0]}' * 10, f'Medidas', f'{formatacao[5]}-{formatacao[0]}' * 10)  #
        sleep(1)

        print(f'{formatacao[1]}AC:{formatacao[0]} {ac}'), sleep(1)
        print(f'{formatacao[1]}BC:{formatacao[0]} {bc}'), sleep(1)
        print(f'{formatacao[1]}AB:{formatacao[0]} {ab}'), sleep(1)

        linha(simb='-', cor=5, tmn=29)  # Linha amarela

        print()  # Quebra de linha
        sleep(1)

        # --------- Resultado ---------
        print(f'{formatacao[5]}-{formatacao[0]}' * 9, f'Resultado', f'{formatacao[5]}-{formatacao[0]}' * 9)
        sleep(1)

        # Verificar se com os dados é possível formar um triângulo
        if ac + bc > ab and ac + ab > bc and bc + ab > ac:  # É possível?
            # calculos
            area_t = area(ac, bc, ab)  # área
            p = peri(ac, bc, ab)  # perímetro
            angs = angulos(ac, bc, ab)  # ângulos
            alts = altura(ac, bc, ab, area_t)  # alturas

            # saída
            # Tipo
            print(f'{formatacao[1]}Tipo:{formatacao[0]} {formatacao[0]}', end='')
            if ac == bc == ab:
                print('Equilátero', end='')
            elif ac == bc or bc == ab or ac == ab:
                print('Isósceles', end='')
            else:
                print('Escaleno', end='')

            if 90 in angs:
                print(' - Triângulo retângulo', end='')
            sleep(1)

            # Área e perímetro
            print(f'\n\n{formatacao[1]}Área:{formatacao[0]} {area_t:.2f}'), sleep(1)
            print(f'{formatacao[1]}Perímetro:{formatacao[0]} {p:.2f}'), sleep(1)

            # Ângulos
            print(f'\n{formatacao[1]}Ângulo A:{formatacao[0]} {angs[0]:.2f}°'), sleep(1)
            print(f'{formatacao[1]}Ângulo B:{formatacao[0]} {angs[1]:.2f}°'), sleep(1)
            print(f'{formatacao[1]}Ângulo C:{formatacao[0]} {angs[2]:.2f}°'), sleep(1)

            # Alturas
            print(f'\n{formatacao[1]}Altura A:{formatacao[0]} {alts[0]:.2f}'), sleep(1)
            print(f'{formatacao[1]}Altura B:{formatacao[0]} {alts[1]:.2f}'), sleep(1)
            print(f'{formatacao[1]}Altura C:{formatacao[0]} {alts[2]:.2f}')

        else:  # Não é possível...
            print('Com esses dados, não é \npossível formar um triângulo!')
        sleep(1)
        linha(simb='-', cor=5, tmn=29)  # Linha amarela
        print()
        sleep(1.5)

    linha(cor=3)
