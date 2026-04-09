"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne
por cliente.

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de
5% sobre o total da compra.

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra:
    tipo de carne
    quantidade de carne
    preço total
    tipo de pagamento
    valor do desconto
    valor a pagar.
"""

file = 4.9
alcatra = 5.9
picanha = 6.9

print(f'{"Ate 5 Kg":>31}{"Acima de 5Kg":>21}')
print(f'{"File Duplo":<8} {"R$ 4,90 por Kg":>20} {"R$ 5,80 por Kg":>20}')
print(f'{"Alcatra":<8} {"R$ 5,90 por Kg":>22} {"R$ 6,80 por Kg":>20}')
print(f'{"Picanha":<8} {"R$ 6,90 por Kg":>22} {"R$ 7,80 por Kg":>20}')

tipo = str(input('\nInsira qual carne voce quer comprar: ')).lower()
qtd = float(input('Insira quantos Kgs voce quer comprar: '))

if qtd > 5:
    file += 0.9
    alcatra += 0.9
    picanha += 0.9

if tipo == "file duplo": preco = file
elif tipo == "alcatra": preco = alcatra
elif tipo == "picanha": preco = picanha

print(f'{qtd} Kgs de {tipo.capitalize()} custara: R$ {preco * qtd:.2f}')