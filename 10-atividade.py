import os
os.system('cls')

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))


menor_valor = min(num1, num2, num3)
maior_valor = max(num1, num2, num3)

print('\nPrimeiro numero: ', num1)
print('segundo numero: ', num2)
print('terceiro numero: ', num3)
print('\nO maior numero: ', maior_valor)
print('O menor numero: ', menor_valor)
