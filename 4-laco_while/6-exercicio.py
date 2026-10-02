import os
os.system('cls')

quant_de_nota = 3
soma = 0

for i in range(quant_de_nota):
    while True:
        nota = float(input(f'Digite sua {i+1}º nota: '))
        if nota < 0 or nota > 10:
            print('\nNota inválida, tente novamente!')
            input('Pressione a tecla enter para continuar...')
            os.system('cls')
        else:
            soma += nota
            break

media = soma / quant_de_nota

print(f'\nSua média é {media}')
if media > 7:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')