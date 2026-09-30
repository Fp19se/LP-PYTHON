import os
os.system('cls')
import time
login_certo = 'abc'
senha_certa = '123'

tentativas = 1

while True:
    if tentativas <= 3:
        print(f'Tentativas: {tentativas}')
        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')
        tentativas += 1

        if login == login_certo and senha == senha_certa:
            print('Seja Bem-vindo')
            break
        else:
            print('\nLogin ou senha incorreta, tente novamente')
            print('Tente novamente! ')
            os.system('cls')
    else:
        print('=FIM=')
        break
