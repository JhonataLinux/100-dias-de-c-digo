stock = []

print("Bem vindo JB-stock")

while True:
    print("*--------------------------------*")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar estoque")
    print("4 - Mostrar valor total do estoque")
    print("5 - Sair do sistema")
    print("*--------------------------------*")

    r = input("Qual opção desejada? ")

    if r not in ["1", "2", "3", "4", "5"]:
        print("Opção inválida!")

    elif r == "1":
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        valor = float(input("Digite o valor do produto: "))
        stock.append({"produto": produto, "quantidade": quantidade, "valor": valor})
        print("Produto adicionado com sucesso!")

    elif r == "2":
        if stock:
            for i, c in enumerate(stock, start=1):
                print(f"{i} → {c['produto']} ({c['quantidade']} unid. - R${c['valor']:.2f})")
            posicao = int(input("Digite a posição do item para remover: "))
            if 1 <= posicao <= len(stock):
                stock.pop(posicao - 1)
                print("Produto removido com sucesso!")
            else:
                print("Posição inválida!")
        else:
            print("Nenhum produto no estoque!")

    elif r == "3":
        if stock:
            for i, c in enumerate(stock, start=1):
                print(f"{i} → {c['produto']} | {c['quantidade']} unid. | R${c['valor']:.2f}")
        else:
            print("Nenhum produto encontrado!")

    elif r == "4":
        if stock:
            valor_total = sum(item["quantidade"] * item["valor"] for item in stock)
            print(f"Valor total em estoque: R${valor_total:.2f}")
        else:
            print("Estoque vazio!")

    elif r == "5":
        print("Encerrando sessão... até mais!")
        break
