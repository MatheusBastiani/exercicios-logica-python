"""
Altere o programa anterior permitindo ao usuário informar as populações e as
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
A = int(input('Insira a populacao do pais A: '))
B = int(input('Insira a populacao do pais B: '))

t_A = float(input('Insira a taxa de crescimento do pais A: '))
t_B = float(input('Insira a taxa de crescimento do pais B: '))
anos = 0

while A <= B:
    A = A * (1 + t_A / 100)
    B = B * (1 + t_B / 100)
    anos = anos + 1

print(f'Precisa de {anos} anos para a populacao de A ser maior ou igual a B')