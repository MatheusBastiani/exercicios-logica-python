"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
(em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

fruta = input('Qual fruta voce deseja comprar ? Maca ou Morango ? ').lower()
qtd = float(input('Quantos quilos voce deseja comprar: '))

morango = 2.50
maca = 1.80

if qtd > 5 and qtd < 8:
    morango -= 0.3
    maca -= 0.3



if fruta == "morango": preco = morango * qtd
elif fruta == "maca": preco = maca * qtd

if qtd > 8 or preco > 25: preco = preco * 0.9

print(f'\nCusto total: R$ {preco}')