"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""

dia_semana = int(input('Insira o dia da semana indo de 1 a 7: '))

match dia_semana:
    case 1: print('1-Domingo')

    case 2: print('2-Segunda')

    case 3:print('3-Terca')

    case 4:print('4-Quarta')

    case 5: print('5-Quinta')

    case 6:print('6-Sexta')

    case 7:print('7-Sabado')