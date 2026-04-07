"""
Faça um Programa que peça um número correspondente a um determinado ano e em
seguida informe se este ano é ou não bissexto.
"""

ano = int(input('Informe o ano a ser checado'))

if ano % 4: print(f'{ano} nao e bissexto ')
else: print(f'{ano} e bissexto ')