import os
os.system('cls')
import time
login_certo = 'abc'
senha_certa = '123'


while True:
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')
        if login == login_certo and senha == senha_certa:
            print('Seja Bem-vindo')
            break
        else:
            print('\nLogin ou senha incorreta, tente novamente')
            # time.sleep(2)
            os.system('cls')

