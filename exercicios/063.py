"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
maior = soma = 0
menor = 1000
numeros = []

print('Insira numeros inteiros a serem comparado e somados, digite 0 para o resultado.')

while 1:

    num = int(input())
    numeros.append(num)
    if int(num) > maior and 0 < int(num) < 1000: maior = int(num)
    if int(num) < menor and 1000 > int(num) > 0 != num: menor = int(num)

    if 0 < int(num) < 1000: soma += num

    if num == 0: break

print('O menor numero e: ',menor)
print('O maior numero e: ',maior)
print('A soma de todos os numeros e: ',soma)
