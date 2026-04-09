"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.
"""
primo = par = 0

for i in range(10):
    n = int(input('Insira um numero inteiro: '))
    if n % 2: primo += 1
    else: par += 1

print(f'Foram digitados {par} numeros par e {primo} numeros impar')