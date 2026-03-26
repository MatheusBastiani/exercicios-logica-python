"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

genero = input('Qual seu genero').upper()

if genero == 'F': print('Feminino')
elif genero == 'M': print('Masculino')
else: print('Sexo invalido')