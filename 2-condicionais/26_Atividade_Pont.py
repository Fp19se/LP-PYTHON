import os
os.system('cls')

print('''
===Tabela de Preços===
FRUTAS            5KG                     ACIMA DE 5KG
Morango           R$ 2,50 por Kg          R$ 2,20
Maçã              R$ 1,80 por Kg          R$ 1,50
''')

qtd1 = int(input('Digite a quantidade em Kg de Morango: '))
qtd2 = int(input('Digite a quantidade em Kg de Maça: '))

morango_5kg = 2.50
morango_acima_5kg = 2.20
maca_5kg = 1.80
maca_acima_5kg = 1.50

if qtd1 <= 5:
    conta = morango_5kg * qtd1
elif qtd2 <= 5:
    conta1 = maca_5kg * qtd2
elif qtd1 > 5:
    conta2 = morango_acima_5kg * qtd1
elif qtd2 > 5:
    conta3 = maca_acima_5kg * qtd2

