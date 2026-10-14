import os
os.system('cls')

print('= IMSERINDO NÚMEROS NO VETOR =')
vetor_numeros = []

numero = int(input('Digite um número: '))
vetor_numeros.append(numero)
numero = int(input('Digite um número: '))
vetor_numeros.append(numero)
numero = int(input('Digite um número: '))
vetor_numeros.append(numero)

print('\n= EXIBINDO NÚMEROS DO VETOR =')
print(f'Primeira posição do vetor: {vetor_numeros[0]}')
print(f'Última posiçao do vetor: {vetor_numeros[2]}')

