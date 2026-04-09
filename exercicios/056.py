"""
Altere o programa anterior para mostrar no final a soma dos números.
"""
soma = 0

n1 = int(input('Insira um numero inteiro: '))
n2 = int(input('Insira o segundo numero inteiro: '))

for i in range(n1 + 1, n2):
    soma += i

print('\nSoma = ',soma)