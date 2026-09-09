import os
os.system('cls')

print('''
===CARDAPIO===
(1) PICANHA - R$ 25,00
(2) LASANHA - R$ 20,00
(3) STROGONOFF - R$ 18,00
(4) BIFE ACEBOLADO R$ 15,00
(5) PÃO COM OVO - R$ 5,00
''')

numero = int(input('Digite o número no cardapio: '))



match numero:
    case 1:
        print('\nO prato é picanha e o valor é: R$ 25,00')
    case 2:
        print('\nO prato é lasanha e o valor é: R$ 20,00')
    case 3:
        print('\nO prato é strogonoff e o valor é: R$ 18,00')
    case 4:
        print('\nO prato é bife acebolado e o valor é: R$ 15,00')
    case 5:
        print('\nO prato é pão com ovo e o valor é: R$ 5,00 ')