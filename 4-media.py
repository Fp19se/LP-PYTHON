import os


os.system('cls')

print('= SOLICINTADO DADOS =')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
primeira_nota = float(input("Digite sua Primeira nota: "))
segunda_nota = float(input('Digite sua Segunda nota: '))

media = (primeira_nota + segunda_nota) / 2



print('/n= EXBINDO DADOS =')
print('Nome: ', nome)
print('Idade: ', idade)
print('Primeira nota: ', primeira_nota)
print('Segunda_nota: ', segunda_nota)
print('Média: ', media)

