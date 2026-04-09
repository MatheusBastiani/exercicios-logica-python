"""
Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
"""

maior = menor = soma = 0
numeros = []

print('Insira numeros inteiros a serem comparado e somados, digite 0 para o resultado.')

while 1:

    num = int(input())
    numeros.append(num)
    if int(num) > maior: maior = int(num)
    if int(num) < menor and num != 0: menor = int(num)

    soma += num

    if num == 0: break

print('O menor numero e: ',menor)
print('O maior numero e: ',maior)
print('A soma de todos os numeros e: ',soma)
