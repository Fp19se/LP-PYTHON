import os
os.system('cls')

vetor_numero = []
QUANTIDADE_DE_NUMEROS = 6
pares = 0
impares = 0
soma_pares = 0
soma_geral = 0


for i in range(QUANTIDADE_DE_NUMEROS):
    numero = int(input(f'Digite o {i+1}ª número: '))
    vetor_numero.append(numero)
    if numero % 2 == 0:
            pares += 1
    else:
            impares += 1

print('\n= EXIBINDO OS NÚMEROS DO VETOR = ')
for indice, numero in enumerate(vetor_numero, start=1):
    print(f'{indice}º número: {numero}')

print('\n= EXIBINDO OS NÚMEROS PARES E IMPARES DO VETOR = ')
print(f'\nQuantidade de pares: {pares}')
print(f'Quantidades de impares: {impares}')