import os
os.system('cls')

while True:
    nota = int(input('Digite a sua nota: '))
    if nota < 1 or nota > 10:
        print('\nNota inválida, tente novamente!')
    else:
        # print('\nO núm esta entre 1 e 10.')
        break # serve para parar o laço de repetição

print(f'\nSua nota é {nota}')
if nota > 6:
    print('APROVADO')
else:
    print('REPROVADO')


print('=FIM=')