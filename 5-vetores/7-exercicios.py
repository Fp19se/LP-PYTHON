import os
os.system('cls')

QUANTIDADE_DE_NOTAS = 4
vetor_notas = []


for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    vetor_notas.append(nota)

media = sum(vetor_notas) / QUANTIDADE_DE_NOTAS



print('\n= EXIBINDO A NOTAS = ')
for indice, nota in enumerate(vetor_notas, start=1):
    print(f'{indice}º nota: {nota}')
print(f'\nSua média: {media}')


if media >= 7:
    print('APROVADO')
elif media >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')