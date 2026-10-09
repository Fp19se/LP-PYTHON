import os
os.system('cls')
import time




soma = 0
contador = 0


while True:
    print('''
Código  |   Descrição

1       |   Adicionar pessoa

2       |   Exibir resultados

3       |   Sair
''')
    numero = int(input('Qual opção escolhida: '))


    match numero:
        case 1:
            idade = int(input('\nDigite sua idade: '))
            sexo = input('Digite seu sexo (M) ou (F): ').upper()
            salario = float(input('Digite seu salário: '))
            soma += salario
            contador += 1
            
            time.sleep(1)
            os.system('cls')
        case 2:
            media = soma / contador
            print(f'A média de sálario do grupo é {media}')
