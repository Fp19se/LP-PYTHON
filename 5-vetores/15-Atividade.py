import os
os.system('cls')

lista_paciente = []

while True:
    os.system("cls")
    print("""

1 - Cadastrar Paciente
2 - Listar todos os Pacientes
3 - Atualizar Paciente
4 - Remover Paciente
0 - Sair
""")

    opcao = int(input(" Escolha uma opção: "))


    match opcao:
        case 1:
            print('\n== CADASTRAR PACIENTE ==')
            nome_paciente = str(input('Digite o nome completo do paciente do paciente: ')).strip().upper()
            if nome_paciente == '':
                print('\nO nome do paciente deve ser inserido...')
            elif nome_paciente in lista_paciente:
                print('\nEsse paciente já foi cadastrado...')
            else:
                lista_paciente.append(nome_paciente)
                print('\nPaciente cadastrado com sucesso')

        case 2:
            print('\n== LISTAR PACIENTE ==')
            for paciente in lista_paciente:
                print(f'- {paciente}')

        case 3:
            print('\n== ATUALIZAR  PACIENTE ==')
            nome = str(input('Qual paciente deseja atualizar? '))
            if nome in lista_paciente:
                posicao = lista_paciente.index(nome)
                novo = input('Novo nome: ')
                lista_paciente[paciente] = novo
                print('Paciente alterado com sucesso!')
            else:
                print('Paciente não encontrado.')
        case 4:
                print('\n== REMOVER PACIENTE ==')
                nome = str(input('Qual paciente deseja atualizar? '))
                if nome in lista_paciente:
                    lista_paciente.remove(nome)
                    print('Paciente excluido com sucesso')
                else:
                    print('Paciente não encontrado')

        case 0:
            print('Saindo do programa...')
            break

        case _:
            print("Opção inválida! \n Tente novamente...")

    input("Pressione qualquer tecla para continuar")