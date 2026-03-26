"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""

import math

tamanho_MB = float(input('Insira a quantidade de MB presentes no arquivo'))
dowload_Mbps = float(input('Insira a velocidade de dowload em Mbps'))

dowload_MBps = dowload_Mbps / 8

tempo_total_segundo = tamanho_MB / dowload_MBps

minutos = int(tempo_total_segundo // 60)
segundos = int(tempo_total_segundo % 60)


print(f'Voce vai demorar {minutos}:{segundos:02} minutos para baixar o arquivo')
