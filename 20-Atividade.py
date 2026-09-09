import os
os.system('cls')

print('''
===MÊSES DO ANO===

(1) JANEIRO
(2) FEVEREIRO
(3) MARÇO
(4) ABRIL
(5) MAIO
(6) JUNHO
(7) JULHO
(8) AGOSTO
(9) SETEMBRO
(10) OUTUBRO
(11) NOVEMBRO
(12) DEZEMBRO
''')
num = int(input('Digite um número para o mês do ano: '))

match num:
    case 1:
        print('\nJANEIRO')
    case 2:
        print('\nFEVEREIRO')
    case 3:
        print('\nMARÇO')
    case 4:
        print('\nABRIL')
    case 5:
        print('\nMAIO')
    case 6:
        print('\nJUNHO')
    case 7:
        print('\nJULHO')
    case 8:
        print('\nAGOSTO')
    case 9:
        print('\nSETEMBRO')
    case 10:
        print('\nOUTUBRO')
    case 11:
        print('\nNOVEMBRO')
    case 12:
        print('\nDEZEMBRO')
