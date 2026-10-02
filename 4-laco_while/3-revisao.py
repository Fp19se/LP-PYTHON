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

    match produto:
            case 1:
                print('\nSeu pedido é Pastel e o valor R$ 6,00')
                break
            case 2:
                print('\nSeu pedido é coxinha e o valor é R$ 5,00')
                break
            case 3:
                print('\nSeu pedido é bauru e o valor é R$ 7,00')
                break
            case 4:
                print('\nSeu pedido é geladinho e o valor é R$ 2,00')
                break
            case 5:
                print('\nSeu pedido é misto e o valor é R$ 4,00')
                break