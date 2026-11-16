import os
os.system('cls')

quantidade = 3
vetor_nota = []

def calcular_notas(vetor_nota):
    return sum(vetor_nota) / len(vetor_nota)

def mostrar_resultados(media, vetor_notas):
    print('\n= EXIBINDO DADOS =')
    for nota in vetor_nota:
        print(f'Nota: {nota}')

    print(f'\nMédia: {media}')

print('= SOLICITANDO DADOS =')
for i in range(quantidade):
    nota = float(input(f'Digite sua {i+1}ª nota: '))
    vetor_nota.append(nota)

media = calcular_notas(vetor_nota)

mostrar_resultados(media, vetor_nota)