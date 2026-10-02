import os
os.system('cls')

soma = 0
quant_de_notas = 2

for i in range(quant_de_notas):
    while True:
        nota = int(input(f'Digite sua {i+1}ª nota: '))
        if nota < 0 or nota > 10:
            print('Nota inválida, tente novamente!')
            input('Pressione qualquer tecla para continuar...')
            os.system('cls')
        else:
            soma += nota
            break

media = soma / quant_de_notas

print(f'Sua media é {nota}')