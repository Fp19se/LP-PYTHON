
import os
os.system('cls')
primeiro_numero = float(input('DIgite o primeiro numero: '))
segundo_numero = float(input('Digite o segundo numero: '))

soma = primeiro_numero + segundo_numero
media = soma / 2
produto = primeiro_numero * segundo_numero


if primeiro_numero == segundo_numero:
    print('Os numeros são iguais')
else:
    menor_valor = min(primeiro_numero, segundo_numero)
    maior_valor = max(primeiro_numero, segundo_numero)
print('Maior: ', maior_valor)
print('Menor: ', menor_valor)




print('Soma: ', soma)
print('media:', media)
print('produto', produto)
