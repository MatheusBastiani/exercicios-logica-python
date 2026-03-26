"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
n1 = input('Insira o primeiro preco: ')
n2 = input('Insira o segundo preco: ')
n3 = input('Insira o terceiro preco: ')

if n1 < n2 and n1 < n3: print('n1')
elif n2 < n1 and n2 < n3: print('n2')
else: print('n3')

