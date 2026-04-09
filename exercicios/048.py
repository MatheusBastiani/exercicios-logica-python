"""
Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
"""

def perguntar_nome():

    while True:

        nome = str(input('Insira seu nome: ')).casefold()

        if len(nome) > 3:
            return str(nome).capitalize()
        print('\nNome Invalido\n')


def perguntar_idade():
    while True:

        idade = int(input('Insira sua idade: '))

        if 0 < idade < 150:
            return int(idade)
        print('\nIdade Invalida\n')


def perguntar_salario():
    while True:

        salario = float(input('Insira seu salario: '))

        if salario > 0:
            return float(salario)
        print('\nSalario Invalido\n')


def perguntar_sexo():
    while True:

        sexo = str(input('Insira seu genero: ')).casefold()

        if sexo == 'feminino' or sexo == 'masculino':
            return str(sexo).capitalize()
        print('\nSexo Invalido\n')


def perguntar_estado():
    while True:

        estado = str(input('Insira seu estado civil, Solteiro ou Casado: ')).casefold()

        if estado == 'solteiro' or estado == 'casado':
            return str(estado).capitalize()
        print('\nEstado civil invalido\n')

nome = perguntar_nome()
idade = perguntar_idade()
salario = perguntar_salario()
sexo = perguntar_sexo()
estado = perguntar_estado()

print(nome)
print(idade)
print(f'{int(salario)}')
print(sexo)
print(estado)