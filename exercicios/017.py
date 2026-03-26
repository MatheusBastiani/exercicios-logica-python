"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas
e os respectivos preços em 3 situações:

    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.
        Acrescente 10% de folga e sempre arredonde os valores para cima,
        isto é, considere latas cheias.
"""

import math

metro_2 = float(input('Insira a quantidade de metros quadrados a serem pintados: '))

l_tinta = (metro_2 / 6) * 1.1


qtd_lata = math.floor(l_tinta / 18)

qtd_galao = math.ceil((l_tinta % 18) / 3.6)

if qtd_galao >= 5 :
    qtd_galao -= 5
    qtd_lata += 1

print(f'Comprando apenas latas de 18 litros voce pagaria R$ {math.ceil(l_tinta / 18) * 80}')
print(f'Comprando apenas galoes de 3.6 litros voce pagaria R$ {math.ceil(l_tinta / 3.6) * 25}')
print(f'Comprando latas e galoes voce gastaria R$ {qtd_galao * 25 + qtd_lata * 80} em galoes e latas de tinta ')
