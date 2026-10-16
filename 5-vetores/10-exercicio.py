import os
os.system('cls')

vetor_numero = []
soma = 0
negativo = 0

for i in range(5):
    numero = int(input(f'Digite {i+1}ª número: '))
    vetor_numero.append(numero)
    if numero > 0:
        soma = sum(vetor_numero)
    else:
        negativo += 1


print(f'\nNúmeros negativos: {negativo}')
print(f'A soam dos positivos: {soma}')