inventario = {'notbook' :3, 'memoria ram 15g' :9, 'processando': 10, 'gabinete':2}

def gerenciar_inventario(inventario,produto, quantidade_movimentada):
    if produto in inventario:
        print("Ja Existe")
        inventario[produto] = inventario[produto] + quantidade_movimentada
    else:
        inventario[produto] = quantidade_movimentada
def checar_inventario(inventario, produto, venda_produto):
    if  inventario[produto] >= venda_produto:
        inventario[produto] =- venda_produto
        print(f"venda do produto {produto}: unidade {venda_produto}")
        print(f"Novo estoque: {produto}: {inventario[produto]}")
    else:
        print(f" Quantidade de produto insuficiente em estoque: {produto}")



gerenciar_inventario(inventario, 'notbook', 10)
gerenciar_inventario(inventario, 'mouse gamer', 16)
checar_inventario(inventario, 'notbook', 10)
checar_inventario(inventario, 'gabinete', 5)

print("\n --- Invetario atual ---")
print(inventario)
