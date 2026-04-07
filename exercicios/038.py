"""
Faça um Programa para um caixa eletrônico.

O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas.

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.

O programa não deve se preocupar com a quantidade de notas existentes na
máquina.

Exemplo 1:
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2:
Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""


saque = int(input('Insira a quantidade de dinheiro a ser sacado (entre 10 a 600 reais): \n'))
saque_aux = saque

n_100 = saque_aux // 100
saque_aux = saque_aux - n_100 * 100

n_50 = saque_aux // 50
saque_aux = saque_aux - n_50 * 50

n_10 = saque_aux // 10
saque_aux = saque_aux - n_10 * 10

n_5 = saque_aux // 5
saque_aux = saque_aux - n_5 * 5

n_1 = saque_aux


print(f'{"Saque:":<30} {saque:>8}')
print(f'{"Notas de 100:":<30} {n_100:>8}')
print(f'{"Notas de 50:":<30} {n_50:>8}')
print(f'{"Notas de 10:":<30} {n_10:>8}')
print(f'{"Notas de 5:":<30} {n_5:>8}')
print(f'{"Notas de 1:":<30} {n_1:>8}')
