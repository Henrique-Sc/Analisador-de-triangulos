from ..format import *
from math import sqrt, degrees
from numpy import arccos


def area(a, b, c):
    s = (a + b + c) / 2  # S - Para realizar a equação de Heron
    area = sqrt(s * (s - a) * (s - b) * (s - c))  # Área
    return area


def p(a, b, c):
    peri = a + b + c
    return peri


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

        for cont in f'\nMedidas: \n\ta = {a} \n\tb = {b} \n\tc = {c}\n':
            print(cont, end="")
            sleep(0.25)

        sleep(1)

        if a + b > c and a + c > b and b + c > a:
            area(a, b, c)
            p(a, b, c)
        else:
            print('Com esses dados, não é possível formar um triângulo!')
        sleep(1.5)
