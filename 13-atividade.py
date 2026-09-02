import os
os.system('cls')
#entrada
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))


#processo

imc = (altura * altura) / peso

if imc < 18.5:
    print('Abaixo do peso')
elif imc > 18.6:
    print('Peso ideal')
elif imc <= 25.0:
    print('Levemente acima do peso')
elif imc <= 30.0:
    print('Obesidade grau I')
elif imc <= 35.0:
    print('Obesidade II (severa)')
else:
    print('Obesidade III (mórbida)')

