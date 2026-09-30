import os
os.system('cls')
import time
login_certo = 'abc'
senha_certa = '123'

for i in range(3):
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')
    if login == login_certo and senha == senha_certa:
        print('Seja Bem-vindo')
        break
    else:
        print('Login ou senha incorreta, tente novamente')
        os.system('cls')
        time.sleep(1)
