"""
Faça um Programa que leia três números e mostre o maior deles.
"""

n1 = input('Insira o primeiro numero: ')
n2 = input('Insira o segundo numero: ')
n3 = input('Insira o terceiro numero: ')

if n1 > n2 and n1 > n3: print(f'{n1}')
elif n2 > n1 and n2 > n3: print(f'{n2}')
else: print(f'{n3}')

