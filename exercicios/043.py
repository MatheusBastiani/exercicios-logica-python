"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

gasolina = 2.50
alcool = 1.90

if input('Tecle A caso queira comprar ALCOOL e G caso queira GASOLINA: ').upper() == 'A': preco = 1.90
else: preco = 2.50

litros = float(input('Insira a quantidade de combustivel: '))

if preco == 1.90 and litros <= 20: preco = preco * 0.97
elif preco == 1.90 and litros > 20: preco = preco * 0.95

if preco == 2.50 and litros <= 20: preco = preco * 0.96
elif preco == 2.50 and litros > 20: preco = preco * 0.94

print(f'Voce tera que pagar R$ {preco * litros}. ')