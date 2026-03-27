"""
Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é:
    equilátero, isósceles ou escaleno.

Dicas:
    Três lados formam um triângulo quando a soma de
        quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""

l1 = int(input('Insira o tamanho do primeiro lado: '))
l2 = int(input('Insira o tamanho do segundo lado: '))
l3 = int(input('Insira o tamanho do terceiro lado: '))

if l1 == l2 == l3: print('Triangulo Equilatero')
elif l1 != l2 != l3 : print('Trianguilo Escaleno')
else: print('Triangulo Isosceles')
