import os
os.system('cls')

pares = 0
impares = 0

for i in range(5):
    num = int(input(f'Digite {i+1}º numero: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Quantidade de pares: {pares}')
print(f'Quantidades de impares: {impares}')