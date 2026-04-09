"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
usuário informe um valor válido.
"""

while 1:
    numero = float(input('Insira uma nota entre 0 a 10: '))

    if 0 < numero < 10: exit()
    else: print('Numero invalido.\n')
