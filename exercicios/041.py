"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
operação ele deseja realizar.

O resultado da operação deve ser acompanhado de uma
frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
"""
import math

def positivo_inteiro(entrada):

    if entrada >= 0: print('Numero Positivo')
    else: print('Numero Negativo')

    if math.floor(entrada) == entrada: print('Numero Inteiro')
    else: print('Numero Decimal')

"Inicio do Codigo"

n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))

instrucao = str(input('Insira uma operacao basica a fazer, soma; subtracao; divisao; multiplicacao: '))

if instrucao == "soma":
    result = n1 + n2
    print(result)
    positivo_inteiro(result)

elif instrucao == "subtracao":
    result = n1 - n2
    print(result)
    positivo_inteiro(result)

elif instrucao == "multiplicacao":
    result = n1 * n2
    print(result)
    positivo_inteiro(result)

elif instrucao == "divisao":
    result = n1 / n2
    print(result)
    positivo_inteiro(result)

else:
    print('Entrada invalida')
    exit()