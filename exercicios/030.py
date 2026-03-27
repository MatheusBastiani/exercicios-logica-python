"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita).

O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

valor_hora = float(input('Insira o valor da sua hora: '))
hora_trabalhada = float(input('Insira a quantidade de horas trabalhadas no mes: '))

salario = valor_hora * hora_trabalhada

if salario <= 900: IR = 0
elif salario > 900 and salario <= 1500 : IR = 0.1
elif salario > 1500 and salario <= 2500 : IR = 0.15
else : IR = 0.2

desconto_IR = IR * salario
desconto_INSS = 0.10 * salario
desconto_FGTS = 0.11 * salario
total_desconto = desconto_IR + desconto_INSS + desconto_FGTS
salario_liquido = salario - total_desconto

print(f'{"Salario Bruto":<30} {salario:>8.2f}')
print(f'{"Imposto de Renda":<30} {desconto_IR:8.2f}')
print(f'{"INSS:":<30} {desconto_INSS:>.2f}')
print(f'{"FGTS:":<30} {desconto_FGTS:>.2f}')
print(f'{"Total de Descontos":<30} {total_desconto:>.2f}')
print(f'{"Salario Liquido":<30} {salario_liquido:>.2f}')
