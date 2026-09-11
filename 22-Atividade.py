import os
os.system('cls')

altura = float(input('Digite sua altura: '))
sexo = str(input('Digite seu sexo: ')).upper()

peso_m = (72.7 * altura) - 58
peso_f = (62.1 * altura) - 44.7

match sexo:
    case 'M':
        print('Seu peso ideal: ', peso_m)
    case 'F':
        print('Seu peso ideal: ', peso_f)