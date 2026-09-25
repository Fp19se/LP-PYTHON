import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIAVEL')

soma = 0

for i in range(3):
    soma += int(input('\nDigite um numero para somar: '))


print(f'\nValor final da variavel soma: {soma} ')
