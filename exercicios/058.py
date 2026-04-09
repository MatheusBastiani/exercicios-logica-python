"""
Faça um programa que peça dois números, base e expoente,
calcule e mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.
"""

numero = int(input('Insira a base: '))
expoente = int(input('Insira o expoente'))
numero_aux = numero

while expoente > 1:

    numero = numero * numero_aux
    expoente -= 1

print(numero)