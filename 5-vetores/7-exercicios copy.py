import os
os.system('cls')

QUANTIDADE_DE_NOTAS = 4
vetor_notas = []


for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    vetor_notas.append(nota)

media = sum(vetor_notas) / QUANTIDADE_DE_NOTAS
menor_nota = min(vetor_notas)
maior_nota = max(vetor_notas)

if media >= 7:
    resultado = ('APROVADO')
elif media >= 5:
    resultado =('RECUPERAÇÃO')
else:
    resultado =('REPROVADO')

print('\n= EXIBINDO A NOTAS DO VETOR = ')
for indice, nota in enumerate(vetor_notas, start=1):
    print(f'{indice}º nota: {nota}')


print('\n= EXIBINDO A MÉDIAS DAS NOTAS DO VETOR = ')
print(f'\nSua média: {media}')
print(f'Resultado: {resultado}')

print(f'\n= EXIBINDO A MENOR E A MAIOR NOTA =')
print(f'Menor nota: {menor_nota}')
print(f'Maior nota: {maior_nota}')