import os
os.system('cls')

lista_produtos = []

while True:
    #Limpa o terminal.
    os.system('cls')

    #Menu do programa
    print('''
== MERCADO ==
1 - Cadastrar produtos
2 - Listar produtos
0 - sair
''')


    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            print('\n== CADASTRAR UM PRODUTO ==')
            # strip() retira os espaços vazios no final.
            #upper() todas as letras maiúsculas.
            nome = input('Nome do novo produto: ').strip().upper()

            if nome == '':
                print('O nome não pode ficar vazio.')
            elif nome in lista_produtos:
                print(f'{nome} já foi cadastrado.')
            else:
                # .append(nome) adiciona o nome do produto na lista.
                lista_produtos.append(nome)
                print('Produto cadastrado com sucesso!')
            input('\nPressione uma tecla para continuar...')
        
        case 2:
            print('\n== PRODUTOS NO ESTOQUE ==')
            if len(lista_produtos) == 0:
                print('O estoque está vazio.')
            else:
                for i, produto in enumerate(lista_produtos):
                    print(f'{i+1}. {produto}')
                    #len(lista_produtos) mostra a quantidade de produtos na lista.
                    print(f'Total de produtos: {len(lista_produtos)}')
            input('\nPressione uma tecla para continuar...')
        
        case 0:
            print('Fim do programa.')
            break
        
        case _:
            print('Opção invalida!')
            input('Pressione uma tecla para continuar...')