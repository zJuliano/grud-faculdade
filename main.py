import os

lista_produtos = []
lista_precos = []

msg_erro = None

def msgInicial():
    os.system("clear")
    
    print(f"{"Sistema":=^50}")
    print("Escolha uma das opções:")
    print()
    print(" 1 - Adicionar um produto")
    print(" 2 - Remover um produto")
    print(" 3 - Atualizar um produto")
    print(" 4 - Listar produtos")
    print(" 5 - Sair do programa")
    print(f"{"="*50}")
    print()

def adicionar_produto():

    erro = None

    while True:
        if erro is None:
            nomeProduto = input("Digite o nome do produto que será adicionado: ")
            erro = None

        try:
            precoProduto = float(input("Digite o preço do produto: "))
        except:
            print("Digite um preço válido!")
            erro = True
            continue

        lista_produtos.append(nomeProduto)
        lista_precos.append(precoProduto)

        if lista_produtos and lista_precos:
            print("Produto adicionado!")

            print()
            print("Deseja adicionar outro produto?")
            print("' S ' - Para confirmar e adicionar outro")
            print("' N ' - Para cancelar e voltar ao menu principal")

        confirmacao = input("Digite uma das letras acima [S/N]: ").strip().upper()

        if confirmacao.startswith("S"):
            print("Certo!")
            continue
        else:
            break

def remover_produto():
    if not lista_produtos and not lista_precos:
        print("Nenhum produto cadastrado.")
        input("\nPressione Enter para voltar ao menu...")
        return

    while True:
        print()
        for i, (nome, preco) in enumerate(zip(lista_produtos, lista_precos), start=1):
            print(f"{i}. {nome} - R$ {preco:,.2f}")

        try:
            indice_removido = int(input("Escolha um dos números do produto para remover: "))
        except:
            print("Digite um número válido.")
            continue

        if indice_removido < 1 or indice_removido > len(lista_produtos):
            print("Índice fora do intervalo. Tente novamente.")
            continue

        nome = lista_produtos.pop(indice_removido - 1)
        preco = lista_precos.pop(indice_removido - 1)
        print(f"Removido: {nome} - R$ {preco:,.2f}")

        if lista_produtos and lista_produtos:
            print()
            print("Você ainda tem produtos restantes, deseja remover outro produto?")
            print("' S ' - Para confirmar e remover outro")
            print("' C ' - Para limpar todos os produtos")
            print("' N ' - Para cancelar e voltar ao menu principal")

            confirmacao = input("Digite uma das letras acima [S/C/N]: ").strip().upper()

            if confirmacao.startswith("S"):
                continue
            elif confirmacao.startswith("C"):
                lista_produtos.clear()
                lista_precos.clear()
                print("Todos os produtos foram limpos!")
                input("Pressione Enter para voltar ao menu...")
                break
            elif confirmacao.startswith("N"):
                break
        else:
            input("Pressione Enter para voltar ao menu...")
            break


def indice_valido(produtos, precos, prompt="Escolha um dos números do produto para alterar: "):
    while True:
        print()
        for i, (nome, preco) in enumerate(zip(produtos, precos), start=1):
            print(f"{i}. {nome} - R$ {preco:,.2f}")

        try:
            escolha = int(input(prompt))
        except ValueError:
            print("Digite um número válido.")
            continue

        if 1 <= escolha <= len(produtos):
            return escolha - 1

        print("Índice inválido! Tente novamente.")

def atualizar_produto():

    if not lista_produtos and not lista_precos:
        print("Nenhum produto cadastrado.")
        input("\nPressione Enter para voltar ao menu...")
        return

    
    print("Escolha uma das opções:")
    print()
    print(" 1 - Para alterar o nome do produto")
    print(" 2 - Para alterar o preço do produto")
    print()

    while True:
        try:
            opcao = int(input("Escolha uma das opções acima: "))
        except:
            print("Digite um número válido.")
            continue

        if opcao < 1 or opcao > 3:
            print("Por favor, digite um número entre 1 a 3")
            input("\nPressione Enter para voltar...")
            continue

        if opcao == 1:
            indice = indice_valido(lista_produtos, lista_precos)
            produtoAntes = lista_produtos[indice]

            produtoNovo = input("Digite o novo nome do produto: ")
            lista_produtos[indice] = produtoNovo

            print(f"Nome do produto alterado de {produtoAntes} para {produtoNovo}")
            input("\nPressione Enter para voltar ao menu...")
            break
        elif opcao == 2:
            indice = indice_valido(lista_produtos, lista_precos)
            precoAntes = lista_precos[indice]

            try:
                precoNovo = float(input("Digite o novo preço do produto: "))
            except:
                print("Digite um preço válido!")

            lista_precos[indice] = precoNovo

            print(f"Preço do produto alterado de R$ {precoAntes:,.2f} para R$ {precoNovo:,.2f}")
            input("\nPressione Enter para voltar ao menu...")
            break
        
def listar_produtos():
    if not lista_produtos and not lista_precos:
        print("Nenhum produto cadastrado.")
        input("\nPressione Enter para voltar ao menu...")
        return

    print(f"\nQuantidade de produtos: {len(lista_produtos)}")
    for i, (nome, preco) in enumerate(zip(lista_produtos, lista_precos), start=1):
        print(f"{i}. {nome} - R$ {preco:,.2f}")

    while True:
        input("Pressione Enter para voltar ao menu...")
        break

while True:

    msgInicial()

    if msg_erro:
        print(msg_erro)
        msg_erro = None

    try:
        opcao = int(input("Digite uma das opções acima: "))
    except:
        msg_erro = "Por favor, digite APENAS números"
        continue
    
    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        remover_produto()
    elif opcao == 3:
        atualizar_produto()
    elif opcao == 4:
        listar_produtos()
    elif opcao == 5:
        print("Programa encerrado!")
        break
    else:
        msg_erro = "Por favor, digite um número entre 1 a 5"
        continue