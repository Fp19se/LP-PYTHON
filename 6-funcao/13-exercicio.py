import os
os.system('cls')

quantidade = 2
soma = 0

def nota_0_10():
    if nota >= 0 and nota <= 10:
        soma += nota
    else:
        print()


for i in range(quantidade):
    nota = float(input(f'Digite sua {i+1}ª nota: '))
