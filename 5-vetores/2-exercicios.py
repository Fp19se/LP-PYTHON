import os
os.system('cls')

vetor_notas = []
quant_notas = 3
soma = 0
for i in range(quant_notas):
    nota = float(input('Digite uma nota: '))
    vetor_notas.append(nota) #Inserindo a nota no vetor
    soma += vetor_notas
    media = soma / 3
for i in range(3):
    print(f'Nota: {vetor_notas[i]}')

print(f'A média é: {media}')