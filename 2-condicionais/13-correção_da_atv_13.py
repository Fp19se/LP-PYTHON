import os
os.system('cls')
#entrada

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

#processamento

imc = peso / (altura * altura)

if imc < 18.5:
    resultado = 'abaixo do peso'
elif imc <= 24.9:
    resultado = 'peso ideal (parabens)'
elif imc <= 29.9:
    resultado = 'Levemente acima do peso'
elif imc <= 34.9:
    resultado = 'Obesidade grau I'
elif imc <= 39.9:
    resultado = 'Obesidade II (severa)'
else:
    resultado = 'Obesidade III (mórbida)'


print('\n=RESULTADO=', resultado)
