import os
os.system('cls')

centimetros = 100

def medicao(metro):
    conta = (metro * centimetros)
    print(f'Metros: {metro} - Centímetros: {conta}')
    return

print('= SOLICITANDO DADOS =')
metro = float(input('Digite em valor em metros: '))

print('\n= EXIBINDO DADOS =')
medicao(metro)