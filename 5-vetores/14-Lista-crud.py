import os
os.system("Cls")
# Crud ?

lista_produtos = []

while True:
    os.system("cls")
    print("""
- Mercadinho vN -
1 - Cadastrar Produto
2 - Listar todos os Produtos
3 - Atualizar Produto
4 - Remover Produto
5 - Buscar por Produto
0 - Sair
""")
    
    opcao = int(input(" Escolha uma opção: "))
    
    match opcao:
        case 1:
            # Create ( Criar, Cadastrar )
            print("- Cadastrar Produto - ")
            nome_produto = input("Digite o nome do novo Produto: ").strip().upper()
            if nome_produto == "":
                print("O nome do produto deve ser inserido...")
            elif nome_produto in lista_produtos:
                print("Produto já Cadastrado")
            else:
                lista_produtos.append(nome_produto)
                print("Produto cadastrado com Sucesso!")
                

        case 2:
            # Read ( Filtrar, Buscar )
            print(" - Produtos No Estoque - ")
            for produto in lista_produtos:
                print(f"- {produto}")
            print(f"Total: {len(lista_produtos)}")

        case 3:
            # Update ( Atualizar )
            print("- Atualizar Produto - ")
            nome = input("Qual produto deseja Atualizar? ")
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input("Novo nome: ")
                lista_produtos[posicao] = novo
                print("Produto Alterado com Sucesso!")
            else:
                print("Produto não Encontrado.")

        case 4:
            # Delete ( Remover )
            print("\n- Remover Produto - ")
            nome = input("Qual produto deseja Remover? ")
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print("Produto Excluido com Sucesso!")
            else:
                print("Produto não Encontrado.")

        case 5:
            # Read ( Filtrar, Buscar )
            print("\n- Encontrar Produto - ")
            nome = input("Qual Produto Deseja Encontrar? ")
            if nome in lista_produtos:
                print("Produto Encontrado!")
            else:
                print("Produto não Encontrado.")
            

        case 0:
            print("Saindo do Programa...")
            break

        case _:
            print("Opção inválida! \n Tente novamente...")
            
    input("Pressione qualquer tecla para continuar")