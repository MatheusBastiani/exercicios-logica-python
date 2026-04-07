"""
Faça um Programa que leia um número inteiro maior que 0 e menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros.

Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades

Testar com:
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

while(1):
    n = int(input('Insira um numero inteiro entre 0 e 1000: '))

    qt_unidades = n % 10
    n -= n % 10

    qt_dezenas= int((n % 100) / 10)
    n -= n % 100

    n = str(n)
    qt_centenas = n[0]

    print(f'\n{qt_centenas} centenas, {qt_dezenas} dezenas e {qt_unidades} unidades\n')
