import os
os.system('cls')


soma = 0
quantidade = 0

while True:
    numero = int(input('Digite um número inteiro positivo (ou um negativo para sair): '))

    if numero < 0:
        break

    soma += numero
    quantidade += 1


if quantidade > 0:
    media = soma / quantidade
    print(f'\nA média aritmética dos {quantidade} números digitados é: {media}')
else:
    print('Nenhum número positivo foi digitado.')