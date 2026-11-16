import os
from datetime import date
os.system('cls')

ano_atual = date.today().year

def idade_usuario(ano):
    resultado = (ano_atual - ano)
    print(f'Sua idade é: {resultado} anos')
    return



print('= SOLICITANDO DADOS =')
ano = int(input('Qual o seu ano de nascimento: '))

print('\n= EXIBINDO DADOS =')
idade_usuario(ano)