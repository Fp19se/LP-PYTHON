import os
os.system('cls')


def mostrar_dados(nome, email, telefone):
    print(f'''
Nome: {nome}
Email: {email}
Telefone: {telefone}
''')


def logo_senai():
    print('='*20)
    print('   SENAI - BAHIA')
    print('='*20)

logo_senai()
print('= Solicitando dados =')
print()

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
telefone = input('Digite seu telefone: ')
print()

logo_senai()
print('= Exibindo dados =')
mostrar_dados(nome, email, telefone)
