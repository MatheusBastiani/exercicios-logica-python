"""
Altere o programa de cálculo dos números primos, informando, caso o número não
seja primo, por quais número ele é divisível.
"""

numero = int(input('Insira um numero inteiro a ser checado: '))

divisores =[]

if(numero % 2) == 0:
    print('O numero e divisivel por 2. \n')
    divisores.append(2)

if(numero % 3) == 0:
    print('O numero e divisivel por 3. \n')
    divisores.append(3)

if(numero % 5) == 0:
    print('O numero e divisivel por 5. \n')
    divisores.append(5)

if(numero % 7) == 0:
    print('O numero e divisivel por 7. \n')
    divisores.append(7)

if len(divisores) > 0:
    print(f'{numero} e divisivel por {divisores}')
else: print(f'{numero} e primo')

