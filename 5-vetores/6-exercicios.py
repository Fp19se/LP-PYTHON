import os
os.system('cls')

quant_de_notas = 3
vetor_notas = []
soma = 0

for i in range(quant_de_notas):
    nota = float(input(f'Digite sua {i+1}º nota: '))
    soma += nota
    vetor_notas.append(nota)

print('\n= EXIBINDO A NOTAS = ')
for indice, nota in enumerate(vetor_notas, start=1):
    print(f'{indice}º nota: {nota}')

media = soma / quant_de_notas
print(f'A média é: {media}')