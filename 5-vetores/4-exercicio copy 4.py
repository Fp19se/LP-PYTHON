import os
os.system('cls')

print('= IMSERINDO OS LIVROS NO VETOR =')
vetor_numeros = []

for i in range(5):

    numero = str(input('Digite um livro: '))
    vetor_numeros.append(numero)

print('\n= EXIBINDO OS LIVROS DO VETOR =')
for valor in vetor_numeros:
    print(f'Os livros citados: {valor}')

for indice, livro in enumerate(vetor_numeros, start=1):
    print(f'{indice}º: {livro}')
