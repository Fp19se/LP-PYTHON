import os
os.system('cls')

pares = 0
impares = 0

def verificar_par_impar(numero):
    if numero % 2 == 0:
        resultado = pares
    else:
        resultado = impares
    return(resultado)


print('= SOLICITANDO DADOS =')
numero1 = int(input('Digite o número: '))

resultado = verificar_par_impar()


print('\n= EXIBINDO DADOS =')
print(f'O número {numero1} é {resultado}')