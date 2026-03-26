"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

ganho_hora = float(input('Insira a quantidade de reais que voce ganha por hora: '))

n_hora = float(input('Insira a quantidade de horas que voce trabalhou no mes: '))

salario = ganho_hora * n_hora

print(f'Voce recebeu {salario} R$')