import os
os.system('cls')

print('CADASTRO')
login_cadastrado = input('\nCrie um login: ')
senha_cadastrada = input('Crie sua senha: ')
os.system('cls')

while True:
    login = input('Digite seu login: ')
    senha = input('Digite uma senha: ')
    if login == login_cadastrado and senha == senha_cadastrada:
        print('Seja Bem-vindo')
        break
    else:
        print('Login ou senha incorreta, tente novamente: ')
        input('\nPressione a tecla enter para continuar...')
        os.system('cls')
