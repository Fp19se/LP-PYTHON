import os

os.system('cls')

# solicitando dados

print('= SOLICITANDO DADOS =')
salario = float(input('Digite o seu salário: '))
salario_minimo = float(input(' Digite o valor do salario minimo: '))

# processamento
print('\n = EXIBINDO DADOS =')
divisao = salario / salario_minimo

# saida
print('=\nEXIBINDO DADOS =')
print('O funcionaro recebe: ', divisao, 'vezes o salario minimo')




