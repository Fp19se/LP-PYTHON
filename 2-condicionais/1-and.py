import os
os.system('cls')

#entrada

login = input('Digite seu Usuário: ')
senha = input('Digite sua senha: ')

#processamneto

login_salvo = 'admin'
senha_salva = '1234'

login_esta_correto = login == login_salvo
senha_esta_correta = senha == senha_salva

#saida

if login_esta_correto and senha_esta_correta:
    print('Seja Bem-vindo')
else:
    print('login ou senha invalida')