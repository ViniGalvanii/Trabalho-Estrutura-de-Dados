from cliente import Cliente
from ListaEncadeada import ListaEncadeada
from produto import Produto
from venda import Venda
from fila import Fila
from pilha import Pilha


def exibir_menu():
    print("\n===== MENU ESTOQUE =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar produto")
    print("4 - Listar produtos")
    print("5 - Pesquisar produto")
    print("6 - Realizar venda")
    print("7 - Ver fila de vendas")
    print("8 - Desfazer última operação")
    print("9 - Exibir valor total do estoque")
    print("10 - Exibir valor total de vendas")
    print("11 - Exibir clientes e valores gastos")
    print("12 - Sair")
    print("========================")


def main():
    clientes = ListaEncadeada()
    proximo_id_cliente = 1

    produtos = ListaEncadeada()
    proximo_id_produto = 1

    fila_vendas = Fila()
    proximo_id_venda = 1

    pilha_operacoes = Pilha()

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except:
            print("⚠️ Entrada inválida! Digite um número.")
            continue

        # ================= CLIENTES =================

        if opcao == 1:
            nome = input("Digite o nome do cliente: ").strip()

            if nome == "":
                print("⚠️ Nome não pode ser vazio!")
                continue

            cliente = Cliente(proximo_id_cliente, nome)
            clientes.inserir(cliente)

            print("✅ Cliente cadastrado com sucesso!")
            print(cliente)

            proximo_id_cliente += 1

        elif opcao == 2:
            print("\n--- Lista de Clientes ---")
            clientes.listar()

        # ================= PRODUTOS =================

        elif opcao == 3:
            nome = input("Digite o nome do produto: ").strip()

            if nome == "":
                print("⚠️ Nome não pode ser vazio!")
                continue

            try:
                quantidade = int(input("Digite a quantidade do produto: "))
                preco = float(input("Digite o preço do produto: "))
            except:
                print("⚠️ Quantidade e preço devem ser números!")
                continue

            if quantidade < 0:
                print("⚠️ Quantidade não pode ser negativa!")
                continue

            if preco <= 0:
                print("⚠️ Preço deve ser maior que zero!")
                continue

            produto = Produto(proximo_id_produto, nome, quantidade, preco)
            produtos.inserir(produto)

            print("✅ Produto cadastrado com sucesso!")
            print(produto)

            proximo_id_produto += 1

        elif opcao == 4:
            print("\n--- Lista de Produtos ---")
            produtos.listar()

            if produtos.inicio is None:
                print("⚠️ Nenhum produto cadastrado!")      

        elif opcao == 5:
            try:
                id_pesquisa = int(input("Digite o ID do produto para pesquisar: "))
            except:
                print("⚠️ ID deve ser um número!")
                continue

            produto_encontrado = produtos.buscar_por_id(id_pesquisa)

            if produto_encontrado:
                print("✅ Produto encontrado:")
                print(produto_encontrado)
            else:
                print("⚠️ Produto não encontrado!")

        elif opcao == 6:
            try:
                id_cliente = int(input("Digite o ID do cliente: "))
                id_produto = int(input("Digite o ID do produto: "))
                quantidade = int(input("Digite a quantidade: "))
            except:
                print("⚠️ IDs e quantidade devem ser números!")
                continue

            cliente = clientes.buscar_por_id(id_cliente)
            produto = produtos.buscar_por_id(id_produto)

            if not cliente:
              print("⚠️ Cliente não encontrado!")
              continue

            if not produto:
              print("⚠️ Produto não encontrado!")
              continue

            if quantidade <= 0:
              print("⚠️ Quantidade deve ser maior que zero!")
              continue

            if quantidade > produto.quantidade:
              print("⚠️ Quantidade insuficiente em estoque!")
              continue

            produto.quantidade -= quantidade

            venda = Venda(proximo_id_venda, cliente, produto, quantidade)

            fila_vendas.enqueue(venda)
            pilha_operacoes.push(venda)

            print("✅ Venda realizada com sucesso!")
            print(venda)

            proximo_id_venda += 1

            


        elif opcao == 7:
            print("\n--- Fila de Vendas ---")
            fila_vendas.listar()


        elif opcao == 8:
            ultima = pilha_operacoes.pop()

            if not ultima:
             print("⚠️ Nada para desfazer.")
            else:
                ultima.produto.quantidade += ultima.quantidade
                print("✅ Última venda desfeita:")
                print(ultima)



            

        elif opcao == 9:
            print("Total estoque")

        elif opcao == 10:
            print("Total vendas")

        elif opcao == 11:
            print("Clientes e gastos")

        elif opcao == 12:
            print("Saindo do sistema...")
            break

        else:
            print("⚠️ Opção inválida!")


if __name__ == "__main__":
    main()