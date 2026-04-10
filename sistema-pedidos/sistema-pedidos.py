import json
import os

ARQUIVO = "data.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {"produtos": [], "pedidos": []}
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def adicionar_produto(dados):
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    dados["produtos"].append({"nome": nome, "preco": preco})
    salvar_dados(dados)
    print("Produto adicionado!\n")

def listar_produtos(dados):
    if not dados["produtos"]:
        print("Nenhum produto cadastrado.\n")
        return
    for i, p in enumerate(dados["produtos"], 1):
        print(f"{i} - {p['nome']} (R${p['preco']})")
    print()

def fazer_pedido(dados):
    listar_produtos(dados)
    if not dados["produtos"]:
        return

    escolha = int(input("Escolha o produto: ")) - 1
    quantidade = int(input("Quantidade: "))

    produto = dados["produtos"][escolha]
    total = produto["preco"] * quantidade

    pedido = {
        "produto": produto["nome"],
        "quantidade": quantidade,
        "total": total
    }

    dados["pedidos"].append(pedido)
    salvar_dados(dados)

    print("Pedido realizado!\n")

def listar_pedidos(dados):
    if not dados["pedidos"]:
        print("Nenhum pedido feito.\n")
        return

    for i, p in enumerate(dados["pedidos"], 1):
        print(f"{i} - {p['produto']} | Qtd: {p['quantidade']} | Total: R${p['total']}")
    print()

# Menu
def menu():
    dados = carregar_dados()

    while True:
        print("=== SISTEMA DE PEDIDOS ===")
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Fazer pedido")
        print("4 - Listar pedidos")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_produto(dados)
        elif opcao == "2":
            listar_produtos(dados)
        elif opcao == "3":
            fazer_pedido(dados)
        elif opcao == "4":
            listar_pedidos(dados)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    menu()