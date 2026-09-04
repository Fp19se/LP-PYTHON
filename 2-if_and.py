import os
os.system('cls')

#entrada
nota1 = int(input('Digite sua nota: '))
nota2 = int(input('Digite sua segunda nota: '))
faltas = int(input('Digite quantas faltas voçê tem: '))

#processo

media = (nota1 + nota2) / 2

if media >= 7 and faltas <= 40:
    print('Aprovado')
else:
    print('Reprovado')
#saida
