"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

numeros = []

for i in range(3):
    numeros.append(int(input('Insira um numero')))

ordenados = sorted(numeros)

for i in range(2, -1, -1):
    print(ordenados[i])


