import os
os.system('cls')

dia = int(input('digite o dia da semana: '))

match dia:
    case 2:
        print('Dia útil')
    case 3:
        print('\nDia útil')
    case 4:
        print('\nDia útil')
    case 5:
        print('\nDia útil')
    case 6:
        print('\nDia útil')
    case 7:
        print('Final de semana')
    case 1:
        print('Final de semana')
    case _:
        print("\nDia invalido")



print('=== FIM ===')