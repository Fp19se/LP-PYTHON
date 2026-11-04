import os
os.system('cls')


lista_nome = []
lista_posicao = []
lista_camisa = []

while True:
    os.system("cls")
    print("""

1 - Cadastrar Atleta
2 - Listar todos os Atletas
3 - Atualizar Atletas
4 - Remover Atletas
0 - Sair
""")

    opcao = int(input(" Escolha uma opção: "))


    match opcao:
        case 1:
            print('\n== CADASTRAR ATLETA ==')
            nome = str(input('Digite o nome do atleta: '))
            posicao = input('Digite a posição do atleta: ')
            camisa = input('Digite o número da camisa do atleta: ')
            if nome == '':
                print('\nO cadastro completo do atleta deve ser inserido...')
            elif nome in lista_nome:
                print('\nEsse atleta já foi cadastrado...')
            else:
                lista_nome.append(nome)
        case 2:
            print('\n== LISTAR PACIENTE ==')
            for nome in lista_nome:
                print(f'- {nome}')
        case 3:
            ...
        case 4:
            ...
        case 0:
            print('Saindo do programa...')
            break
        case _:
            print("Opção inválida! \n Tente novamente...")
    
    input("Pressione qualquer tecla para continuar")