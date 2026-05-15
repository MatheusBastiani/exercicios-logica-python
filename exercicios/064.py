"""
Altere o programa de cálculo do fatorial (61), permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos e
menores que 16.
"""
while(1):

    numero = int(input('Insira um numero inteiro menor que 16 diferente de 0: '))
    num_aux = numero

    if(0 < numero <= 16):
        for i in range(numero, 1, -1):
            numero = numero * (i - 1)
        print(f'Fatorial de {num_aux} e: {numero}')

    else: print('Numero invalido')





