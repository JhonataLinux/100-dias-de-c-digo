import sqlite3

DB_NAME = "loja.db"

def conectar():
    conn = sqlite3.connect(DB_NAME)
    return conn

def adicionar_produto(conn,nome, preco, estoque):
    conn.execute("""
    INSERT INTO produtos (nome, preco, estoque)
    VALUES (?, ?, ?)
""",(nome, preco,estoque))
    conn.commit()
    conn.close()
    print(f"Produto '{nome}' adicionado com sucesso!")

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    dados = cursor.fetchall()
    conn.close()
    return dados
  
#------------------------------------------------------
print("Sistema vendas")
while True:
    print("1 - Adicionar novo produtor?")
    print("2 - lista estoque")
    print("3 - sair")

    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        nome = input("Novo produto: ")
        preco = float(input("Preço do produto: "))
        estoque = int(input("Quantidade:  "))
        conn = conectar()
        adicionar_produto (conn, nome, preco, estoque)
        print("produto adicionando com sucesso")
    elif opcao == 2:
        for i in listar_produtos():
            print(f"Lista de estoque {i}")
