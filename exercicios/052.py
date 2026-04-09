"""
Faça um programa que leia 5 números e informe o maior número.
"""
n = 0

for i in range(5):
    aux = float(input('Insira 1 numero: '))
    if aux > n: n = aux
print(n)