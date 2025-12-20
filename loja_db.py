import sqlite3

DB_NAME = "loja.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco  REAL NOT NULL,
    estoque INTEGER NOT NULL)
""")

cursor.execute("SELECT COUNT(*) FROM produtos;")
if cursor.fetchone()[0] ==0:
    print("Criando base de dados novo... \n")
#Insere o produto.
    cursor.execute("""
    INSERT INTO produtos (nome, preco, estoque)
    VALUES (?, ?, ?)
""", ( "Nome", 20.00, 10))
    
    #Atualiza produto no banco de dados
    cursor.execute("""
    UPDATE produtos SET preco = 25.00
    WHERE nome = "Nome"
""")
    #Deletar 
    cursor.execute("""
    DELETE FROM produtos
    WHERE nome = "Nome"
""")
    #print banco de dados 
    cursor.execute("""
    SELECT id, nome, preco, estoque
    FROM produtos
""")
    print(cursor.fetchall())
 
    #fecha sesão
    conn.commit()
    print("Dados inseridos com sucesso!")
conn.close()