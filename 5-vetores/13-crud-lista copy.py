import os
os.system('cls')

lista_series = []

while True:
    #Limpa o terminal.
    os.system('cls')

    #Menu do programa
    print('''
== Serie ==
1 - Cadastrar serie
2 - Listar serie
0 - Sair
''')


    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            print('\n== CADASTRAR UMA SERIE ==')
            # strip() retira os espaços vazios no final.
            #upper() todas as letras maiúsculas.
            nome = input('Nome da nova serie: ').strip().upper()

            if nome == '':
                print('O nome não pode ficar vazio.')
            elif nome in lista_series:
                print(f'{nome} já foi cadastrado.')
            else:
                # .append(nome) adiciona o nome do produto na lista.
                lista_series.append(nome)
                print('serie cadastrada com sucesso!')
            input('\nPressione uma tecla para continuar...')
        
        case 2:
            print('\n== Serie Listada ==')
            if len(lista_series) == 0:
                print('Sem serie citadas.')
            else:
                for i, produto in enumerate(lista_series):
                    print(f'{i+1}. {produto}')
                    #len(lista_series) mostra a quantidade de produtos na lista.
                    print(f'Total de serie: {len(lista_series)}')
            input('\nPressione uma tecla para continuar...')
        
        case 0:
            print('Fim do programa.')
            break
        
        case _:
            print('Opção invalida!')
            input('Pressione uma tecla para continuar...')