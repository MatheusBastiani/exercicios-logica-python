"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""
import math

numero = float(input('Insira um numero: '))

if numero == math.floor(numero): print('O numero e inteiro')
else: print('O numero e decimal')