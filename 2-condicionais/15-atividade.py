import os
os.system('cls')

nota = int(input('Digite uma nota: '))

if nota >= 0 and nota <= 10:
    print('A nota é: ', nota)
else:
    print('A NOTA DEVE SER ENTRE ZERO E DEZ')