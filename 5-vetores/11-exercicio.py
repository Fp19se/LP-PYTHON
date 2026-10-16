import os
os.system('cls')

vetor_numero = []
negativo = 0

for i in range(5):
    numero = int(input(f'Digite o {i+1}ª número: '))
    if numero < 0:
        numero = 0
    vetor_numero.append(numero)

for indice, numero, in enumerate(vetor_numero, start=1):
    print(f'{indice}º: {numero}')
