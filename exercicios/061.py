"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120
"""

numero = int(input('Insira o numero a ser calculado o fatorial: '))

for i in range(numero, 1, -1):
    numero = numero * (i - 1)

print(numero)