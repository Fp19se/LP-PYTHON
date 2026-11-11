import os
os.system('cls')



def cadastrar():
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')

def mostrar_menu():
    print('''
== MENU ==

1 - CADASTRAR
2 - EXIBIR LISTA
0 - SAIR
''')

mostrar_menu()
opcao = input('Escolha uma opção: ')

match opcao:
    case 1:
        cadastrar()
    case 2:
        ...
    case 0:
        ...
    case _:
        ...











