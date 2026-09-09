import os
os.system('cls')

sexo = input('Digite seu sexo: ').lower()
ano = int(input('Digite o seu ano de nascimento: '))

if sexo == 'masculino' and ano <= 2008:
    print('Deve se apresentar')
else:
    print('Não deve se apresentar')
