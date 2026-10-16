import os
os.system('cls')
import time
print('''
(1) Pastel
(2) Coxinha
(3) Bauru
(4) Geladinho
(5) Misto
''')

while True:
    produto = int(input('Qual o número escolhido: '))
    if produto < 1 or produto > 5:
        print('Pedido inexistente, tente novamente.')
        time.sleep(3)
        os.system('cls')
