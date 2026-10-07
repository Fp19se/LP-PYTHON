import os
os.system("cls")

quant_de_notas = 2
soma = 0
contator = 0

while True:
    for i in range(quant_de_notas):
        nota = float(input(f'Digite a {i+1}º nota: '))
    if nota < 0 or nota > 10:
            print('\nNota inválida, tente novamente!')
            input('Pressione a tecla enter para continuar...')
            os.system('cls')
    else:
        soma += nota
        contator += 1
    if contator == 1:
        break

a = input('Deseja inserir mais uma nota (S) ou (N): ').upper()
if a == 'S':
    nota2 = float(input('Digite sua 3º nota: '))
    soma += nota2
    media = soma / quant_de_notas
    print(f'Sua média é {media}')
else:
    media2 = soma / quant_de_notas
    print(f'Sua média é {media2}')