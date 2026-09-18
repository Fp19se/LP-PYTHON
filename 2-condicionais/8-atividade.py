import os

os.system('cls')

# entrada

primeiro_numero = float(input('Digite o primeiro numero: '))
segundo_numero = float(input('Digite o segundo numero: '))


# processamento

soma = primeiro_numero + segundo_numero
media = soma / 2
produto = (primeiro_numero * segundo_numero)






if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = primeiro_numero
    menor = segundo_numero



# saida
print('\n= EXIBINDO DADOS')
print(f'soma:  {soma}')
print(f'media:  {media}')