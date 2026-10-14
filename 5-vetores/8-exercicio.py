import os
os.system('cls')

vetor_numero = []
QUANTIDADE_DE_NUMEROS = 5

for i in range(QUANTIDADE_DE_NUMEROS):
    numero = int(input(f'Digite o {i+1}ª número: '))
    vetor_numero.append(numero)

menor_numero = min(vetor_numero)
maior_numero = max(vetor_numero)


print('\n= EXIBINDO OS NÚMEROS DO VETOR = ')
for indice, numero in enumerate(vetor_numero, start=1):
    print(f'{indice}º número: {numero}')


print(f'\n= EXIBINDO A MENOR E A MAIOR NOTA =')
print(f'\nO menor número: {menor_numero}')
print(f'O maior número: {maior_numero}')
