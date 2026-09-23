import os
os.system('cls')

soma = 0
for i in range(5):
    n =int(input(f'Digite o {i+1}º número: '))
    soma = n + soma

print(f'a soma é: {soma}')