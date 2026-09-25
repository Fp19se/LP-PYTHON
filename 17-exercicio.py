import os
os.system('cls')

soma = 0

for i in range(4):
    nota = float(input(f'digite a {i+1}º nota: '))
    soma += nota


media = soma / 4

print(f'\nSua media é {media}')
