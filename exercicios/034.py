"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax² + bx + c.

O programa deverá pedir os valores de a, b e c e fazer as consistências,
informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo
        grau e o programa não deve fazer pedir os demais valores,
        sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raízes reais.
        Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz
        real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais;
        informe-as ao usuário;
"""
import math

a = int(input('Insira o valor de a: '))

if a == 0:
    print('A equacao nao e do segundo grau')
    exit()

b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))

delta = pow(b,2) - (4 * a * c)

if delta < 0:
    print('A equacao nao possui raizes reais.')
    exit()
elif delta == 0:
    print(f' A raiz da equacao é: {-b / a}')
else:print(f'As raizes sao: x1: {(- b + math.sqrt(delta)) / ( 2 * a)} e x2: {(-b - math.sqrt(delta)) / (2 * a)} ')
