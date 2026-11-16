import os
os.system('cls')


def inflacao(preco):
    if preco < 100:
        resultado = (preco * 0.10) + preco
        print(f'O valor total do produto é: R${resultado}')
    else:
        resultado = (preco * 0.20) + preco
        print(f'O valor total do produto é: R${resultado}')
    return

print('= SOLICITANDO DADOS =')
preco = float(input('Qual o valor do produto: '))

print('\n= EXIBINDO DADOS =')
inflacao(preco)
