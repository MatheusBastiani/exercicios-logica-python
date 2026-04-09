"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

n = 0

for i in range(5):
    n += float(input('Insira um numero: '))

print(n)
print(n / 5)