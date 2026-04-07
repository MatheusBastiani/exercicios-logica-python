"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
é uma data válida.
"""

data = str(input('Insira uma data a ser checada: '))

dia = int(data[0] + data[1])
mes = int(data[3] + data[4])
ano = int(data[6] + data[7] + data[8] + data[9])

if mes in [4 , 6 , 9 ,11]: max_dia = 30
elif mes == 2: max_dia = 28
else : max_dia = 31


if (dia < 0) or (dia > max_dia) or (mes > 12): print('Data Invalida')
else: print(f'{data} e uma data valida')
