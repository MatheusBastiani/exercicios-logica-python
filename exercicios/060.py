"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
"""
num_aux = 0
numero = 1


n = int(input('Insira qual termo da sequencia de fibonacci voce quer descobrir: '))

for i in range(n):

    num_aux2 = numero
    numero = numero + num_aux
    num_aux = num_aux2

print(numero)