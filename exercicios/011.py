"""
Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo.
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
"""

n1_int = int(input('Insira o primeiro numero Inteiro: '))
n2_int = int(input('Insira o segundo numero Inteiro: '))

n_float = float(input('Insira um numero Real: '))

print(f' {n1_int} x {n2_int / 2} = {n1_int * (n2_int / 2)}')

print(f' 3 x {n1_int} + {n_float} = {3 * n1_int + n_float}')

print (f'{n_float} ao quadrado = {pow(2, n_float)}')


