import os
os.system('cls')



quantidade = int(input('Digite a quantidade desejada: '))

if quantidade < 12:
    preco = 1.30
else:
    preco = 1.0

valor_total = quantidade * preco
print(f'Valor total: {valor_total}')
