import os
os.system('cls')

def mostrar_tabuada(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

print('= SOLICITANDO DADOS =\n')
numero = int(input('Digite um número: '))

print('\n= EXIBINDO DADOS =')
mostrar_tabuada(numero)
