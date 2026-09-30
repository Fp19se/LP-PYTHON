import os
os.system('cls')

soma = 0
quantidades_de_notas = 2

for i in range(quantidades_de_notas):
    while True:
        nota = float(input(f'Digite sua {i+1}º nota: '))
        if nota < 0 or nota > 10:
            print('\nNota inválida, tente novamnte')
        else:
            soma += nota
            break



media = soma / quantidades_de_notas
print(f'\nMédia {media}')
print('=FIM=')