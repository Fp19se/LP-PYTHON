import os
os.system('cls')
# ENTRADA.
matricula = input('Digite sua matricula: ')
ano = int(input('Digite seu ano de nascimento: '))
tempo= int(input('Digite o seu tempo de trabalho: '))
# PROCESSO.
nascimento = 2026 - ano

if nascimento >= 65 and tempo >= 30:
    print('\nRequerer a aposentadoria')
else:
    print("\nNão requerer a aposentadoria")
