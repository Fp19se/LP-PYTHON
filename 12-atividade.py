import os
os.system('cls')

nome = str(input('Digite seu Nome: '))
nota_1 = float(input('Digite sua nota: '))
nota_2 = float(input('Digite sua segunda nota: '))

media = (nota_1 + nota_2) / 2

if media >= 9:
    print('\nAprovado')
elif media >= 7.5:
    print('Aprovado')
elif media >= 6:
    print('Aprovado')
elif media > 4:
    print('Reprovado')
else:
    print('Reprovado')


print('Sua média foi: ', media)
