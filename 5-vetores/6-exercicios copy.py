import os
os.system('cls')

quant_de_notas = 3
vetor_notas = []

for i in range(quant_de_notas):
    nota = float(input(f'Digite sua {i+1}º nota: '))
    vetor_notas.append(nota)

# Sum Somar tudo que estar no vetor
# soma = sum(vetor_notas)
# media = soma / quant_de_notas
media = sum(vetor_notas) / quant_de_notas


print('\n= EXIBINDO A NOTAS = ')
for indice, nota in enumerate(vetor_notas, start=1):
    print(f'{indice}º nota: {nota}')
print(f'Sua média: {media}')