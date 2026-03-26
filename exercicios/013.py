"""
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
"""

print('\nEsta e uma calculadora de peso ideal a depender do genero\n')

homem = int(input('Digite 1 se for homem, caso contrario digite 0: \n'))

altura = float(input('Digite sua altura: \n'))

if homem : print(f'Seu peso ideal e {72.7 * altura - 58}')
else : print(f'Seu peso ideal e {62.1 * altura - 44.7}')

