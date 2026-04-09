"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""
aux = 0

print('Responda com S ou N')

if input('Voce telefonou para a vitima ?').upper() == 'S': aux += 1
if input('Voce esteve no local do crime ?').upper() == 'S': aux += 1
if input('Voce mora perto da vitima ?').upper() == 'S': aux += 1
if input('Voce devia para a vitima ?').upper() == 'S': aux += 1
if input('Voce trabalhou com a vitima ?').upper() == 'S': aux += 1


match aux:

    case 2:
            print('Voce e suspeito')
            exit()
    case 3:
            print('Voce e cumplice')
            exit()
    case 4:
            print('Voce e cumplice')
            exit()
    case 5:
            print('Voce e assassino')
            exit()

print('Voce e inocente')