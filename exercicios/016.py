"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""

import math

metro_2 = float(input('Quantos metros quadrados serao pintados: '))

litros_tinta = (metro_2 / 3)
qtd_latas = math.ceil(litros_tinta / 18)

print(f'\nVoce precisa de {qtd_latas} latas de tinta, que equivalem a R$ {qtd_latas * 80:.2f} ')
