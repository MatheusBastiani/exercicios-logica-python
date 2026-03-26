"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

vogal = ['a', 'e','i','o','u']

letra = str(input('Insira uma letra')).lower()

if letra in vogal : print(f'{letra} e uma vogal')
else : print(f'{letra} nao e uma vogal')
