import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIAVEL')

soma = 0

for i in range(3):
    numero = int(input('\nDigite um numero para somar: '))
    soma += numero


print(f'\nValor final da variavel soma: {soma} ')
