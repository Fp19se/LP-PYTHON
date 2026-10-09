import os
os.system('cls')

vetor_nomes = []

for i in range(4):
    nome = str(input('Digite uma nome: '))
    vetor_nomes.append(nome) #Inserindo a nome no vetor

for i in range(4):
    print(f'\nNome: {vetor_nomes[i]}')

