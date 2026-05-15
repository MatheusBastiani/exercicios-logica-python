"""
Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo
e por 1.
"""
while(1):
    numero = int(input('Insira o numero inteiro a ser checado: '))

    if(numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0  or numero % 7 == 0):
        print(f'{numero} nao e primo.')
    else:print('O numero e primo')