import os
os.system('cls')

print('= IMSERINDO NÚMEROS NO VETOR =')
vetor_numeros = []

for i in range(3):

    numero = int(input('Digite um número: '))
    vetor_numeros.append(numero)

print('\n= EXIBINDO NÚMEROS DO VETOR =')
for i in range(3):
    print(f'Valores do vetor: {vetor_numeros[i]}')


