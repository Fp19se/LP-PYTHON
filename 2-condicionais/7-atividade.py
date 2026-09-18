import os

os.system('cls')

# entrada
primeira_nota = float(input('Digite a nota: '))
segunda_nota = float(input('Digite a nota: '))
terceira_nota = float(input('Digite a nota: '))


#processo

media = (primeira_nota + segunda_nota + terceira_nota) / 3





if media >= 7:
    print('VOCÊ ESTÁ REPROVADO COM A MÉDIA: ', media)
else:
    print('VOCÊ ESTÁ APROVADO COM A MÉDIA: ', media)


# saida

print(' fim do programa')
