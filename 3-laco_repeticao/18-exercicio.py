import os
os.system('cls')

soma = 0

for i in range(3):
    nota = float(input(f'Digite a {i+1}º nota: '))
    soma += nota
media = soma / 3
if media >= 7:
    resultado = 'Aprovado'
elif media >= 4:
    resultado = 'Recuperção'
else:
    resultado = 'Reprovado'

print(f'\nSua media é {media}')
print(f'O aluno está {resultado}')
