import os
os.system('cls')

print('=TABUADA=')
numero = int(input('Digite um número: '))

print('\n=Soma=')
for i in range(1, 11):
    print(f'{numero} + {i} = {numero + i}')
print('\n=Subtração=')
for i in range(1, 11):
    print(f'{numero} - {i} = {numero - i}')
print('\n=Multiplicação=')
for i in range(1, 11):
    print(f'{numero} * {i} = {numero * i}')
print('\n=Divisão=')
for i in range(1, 11):
    print(f'{numero} / {i} = {numero / i}')
