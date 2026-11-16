import os
os.system('cls')

quantidade = 2
vetor_nota = []

def calcular_notas(vetor_nota):
    return sum(vetor_nota) / len(vetor_nota)

def mostrar_resultados(media, vetor_notas):
    print('\n= EXIBINDO DADOS =')
    for nota in vetor_nota:
        print(f'Nota: {nota}')

def status_do_aluno(media):
    if media >= 7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    return resultado

print('= SOLICITANDO DADOS =')
while True:
    for i in range(quantidade):
        nota = float(input(f'Digite sua {i+1}ª nota: '))
        if nota >= 0 and nota <= 10:
            vetor_nota.append(nota)
            break
        else:
            print('Nota inválida, tente novamente!\n')


media = calcular_notas(vetor_nota)
status_do_aluno = status_do_aluno(media)

print('\n= EXIBINDO DADOS =')
mostrar_resultados(vetor_notas)
print(f'\nMédia: {media}')
print(f'Situação do aluno: {status_do_aluno}')