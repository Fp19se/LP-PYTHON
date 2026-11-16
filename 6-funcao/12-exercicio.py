import os
os.system('cls')

quantidade = 3
vetor_nota = []

def media(vetor_nota):
    resultado = sum(vetor_nota) / quantidade
    print(f'Sua média é {resultado}')
    return
print('= SOLICITANDO DADOS =')
for i in range(quantidade):
    nota = float(input(f'Digite sua {i+1}ª nota: '))
    vetor_nota.append(nota)

print('\n= EXIBINDO DADOS =')
media(vetor_nota)