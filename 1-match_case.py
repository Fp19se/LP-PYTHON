import os
os.system('cls')

dia = input('Digite dia da semana: ').lower()

match dia:
    case 'segunda':
        print('\nHoje é segunda-feira.')
    case 'terça':
        print('\nHoje é terça-feira')
    case 'quarta':
        print('\nHoje é quarta-feira')
    case 'quinta':
        print('\nHoje é quinta-feira')
    case 'sexta':
        print('\nHoje é sexta-feira')
    case 'sábado' | 'domingo':
        print('\nHoje é final de semana')
    case _:
        print("\nDia invalido")

print(dia)

print('=== FIM ===')
