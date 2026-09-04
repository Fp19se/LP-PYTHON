import os
os.system('cls')

#entrada
nota1 = int(input('Digite sua nota: '))
nota2 = int(input('Digite sua segunda nota: '))
faltas = int(input('Digite quantas faltas voçê tem: '))

#processo

media = (nota1 + nota2) / 2
limite_de_faltas = 40
media_aprovacao = 7


if media >= media_aprovacao and faltas <= limite_de_faltas:
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'
#saida
print(f'\nResultado', resultado)