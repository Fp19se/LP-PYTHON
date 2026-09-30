import os
os.system('cls')

soma = 0
quantidades_de_notas = 2

for i in range(quantidades_de_notas):
    while True:
        nota = float(input(f'Digite sua {i+1}º nota: '))
        if nota >= 0 and nota <= 10:
            soma += nota
            break
        else:
            print('\nNota inválida, tente novamnte')



media = soma / quantidades_de_notas
print(f'\nMédia {media}')
print('=FIM=')