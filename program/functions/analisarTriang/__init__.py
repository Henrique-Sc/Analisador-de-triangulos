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
        sleep(1)

        # Criando as variáveis a, b e c para ficar de fácil acesso
        a = triang[0]
        b = triang[1]
        c = triang[2]

        print()
        linha(simb='-', cor=5)  # Linha amarela
        print(f'Medidas: \n\ta = {a} \n\tb = {b} \n\tc = {c}')
        linha(simb='-', cor=5)  # Linha amarela
        sleep(1)

        linha(simb='-', cor=5)  # Linha amarela
        if a + b > c and a + c > b and b + c > a:
            # calculos
            area_t = area(a, b, c)  # area
            p = peri(a, b, c)  # perímetro
            angs = angulos(a, b, c)  # angulos
            alts = altura(a, b, c, area_t)  # alturas

            # saída
            print(f'Área: {area_t:.2f} | Perímetro: {p:.2f}')
            print(f'ângulo AB: {angs[0]:.2f}° | ângulo BC: {angs[1]:.2f}° | ângulo AC: {angs[2]:.2f}°')
            print(f'Altura A: {alts[0]:.2f} | Altura B: {alts[0]:.2f} | Altura C: {alts[0]:.2f}')

        else:
            print('Com esses dados, não é possível formar um triângulo!')
        linha(simb='-', cor=5)  # Linha amarela
        sleep(1.5)
