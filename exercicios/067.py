"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário.

O programa deverá mostrar também o número de divisões que ele executou para
encontrar os números primos.

Serão avaliados o funcionamento, o estilo e o número de testes (divisões)
executados.
"""
numero = int(input('Insira um numero inteiro: '))
primos = [2, 3, 5, 7]

for i in range(numero, 2, 1):
    if i in primos:
    elif numero % 2: primos.append(i)
    elif numero % 3: primos.append(i)
