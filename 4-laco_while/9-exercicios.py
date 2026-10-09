import os
os.system('cls')

pares = 0
impares = 0
soma_pares = 0
soma_geral = 0

while True:
    numero = int(input('Digite um número inteiro positivo: '))

    if numero == 0:
        break

    if numero > 0:
        soma_geral += numero

        if numero % 2 == 0:
            pares += 1
            soma_pares += numero
        else:
            impares += 1

total_numeros = pares + impares

print(f'\nQuantidade de pares: {pares}')
print(f'Quantidades de impares: {impares}')
if pares > 0:
    media_pares = soma_pares / pares
    print('Média dos valores pares:', media_pares)
else:
    print('Média dos valores pares: Nenhum números par foi digitado.')

if total_numeros > 0:
    media_geral = soma_geral / total_numeros
    print("Média geral dos números lidos:", media_geral)
else:
    print('Média geral: Nenhum número válido foi digitado.')
