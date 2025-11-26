inventario = [
    ("Mouse", 15),
    ("Teclado", 5),
    ("Monitor", 22),
    ("Webcam", 8),
    ("Gabinete", 4),
    ("Mousepad", 30)
]
estoque = [nome for nome, qtd in inventario if qtd < 10]
print(estoque)


logs = [
    ("Alice", 101, "SUCCESS"),
    ("Bob", 201, "FAILED"),
    ("Alice", 102, "FAILED"),
    ("Charlie", 303, "SUCCESS"),
    ("Bob", 202, "SUCCESS"),
    ("Alice", 103, "FAILED")
]
logs_falha = [(nome,id,status) for nome, id, status in logs if nome == "Alice" and status == "FAILED"]
print(logs_falha)

produtos = [
    ("Tênis", "Calçados", 12),
    ("Camisa", "Vestuário", 5),
    ("Bermuda", "Vestuário", 18),
    ("Meia", "Acessórios", 3),
    ("Relógio", "Acessórios", 15),
    ("Jaqueta", "Vestuário", 9)
]

reposicao = [nome for nome, categoria, estoque in produtos if categoria == "Vestuário" and estoque <10]
print(reposicao)

inventario = [
    ("banana", "fruta", 15),
    ("maçã", "fruta", 8),
    ("pera", "fruta", 20),
    ("arroz", "grão", 50),
    ("feijão", "grão", 30),
    ("cenoura", "legume", 12),
    ("batata", "legume", 25),
    ("leite", "laticínio", 18),
    ("queijo", "laticínio", 7),
    ("pão", "padaria", 40)
]

frutas = [nome for nome, tipo, qtd in inventario if tipo == "grão" and qtd >10]
print(frutas)


itens = [
    ("Arroz", "Alimento", 5),
    ("Feijão", "Alimento", 3),
    ("Macarrão", "Alimento", 6),
    ("Açúcar", "Alimento", 2),
    ("Café", "Alimento", 4),
    ("Leite", "Bebida", 12),
    ("Suco de Uva", "Bebida", 7),
    ("Refrigerante", "Bebida", 10),
    ("Água Mineral", "Bebida", 15),
    ("Pão Integral", "Padaria", 8),
    ("Bolo Simples", "Padaria", 3),
    ("Biscoito Cream Cracker", "Padaria", 9),
    ("Detergente", "Limpeza", 5),
    ("Sabão em Pó", "Limpeza", 4),
    ("Desinfetante", "Limpeza", 2),
    ("Esponja", "Limpeza", 10),
    ("Álcool 70%", "Limpeza", 6),
    ("Papel Higiênico", "Higiene", 16),
    ("Shampoo", "Higiene", 3),
    ("Sabonete", "Higiene", 12),
    ("Creme Dental", "Higiene", 5),
    ("Escova de Dentes", "Higiene", 4),
    ("Cotonete", "Higiene", 1),
    ("Pilha AA", "Eletrônico", 12),
    ("Carregador USB", "Eletrônico", 3),
    ("Fone de Ouvido", "Eletrônico", 2),
    ("Lampada LED", "Eletrônico", 8),
    ("Mouse", "Eletrônico", 1),
    ("Caderno", "Papelaria", 6),
    ("Caneta Azul", "Papelaria", 20)
]

repor_eletr = [nome for nome, categoria, qtd in itens if categoria == "Eletrônico" and qtd <5]
repor_ali = [nome for nome, categoria, qtd in itens if categoria == "Alimento" and qtd <3]

print(repor_ali)
print(repor_eletr)

funcionarios = [
    {'nome': 'Alice', 'depto': 'TI', 'salario': 80000},
    {'nome': 'Bob', 'depto': 'Vendas', 'salario': 60000},
    {'nome': 'Charlie', 'depto': 'TI', 'salario': 120000},
    {'nome': 'David', 'depto': 'Marketing', 'salario': 70000},
    {'nome': 'Eve', 'depto': 'Vendas', 'salario': 90000},
    {'nome': 'Fábio', 'depto': 'TI', 'salario': 100000}
]

f_ti = [ p['salario'] for p in funcionarios if p['depto'] == "TI" ]

salario = sum(f_ti) / len(f_ti)
print(f" media de salario TI: {salario:.2f}")


funcionarios_rh = [
    {'nome': 'João', 'depto': 'TI', 'salario': 8800},
    {'nome': 'Marina', 'depto': 'RH', 'salario': 4200},
    {'nome': 'Paulo', 'depto': 'Financeiro', 'salario': 9600},
    {'nome': 'Carla', 'depto': 'Marketing', 'salario': 5200},
    {'nome': 'Rafaela', 'depto': 'TI', 'salario': 11200},
    {'nome': 'Sérgio', 'depto': 'Vendas', 'salario': 7300},
    {'nome': 'Letícia', 'depto': 'Financeiro', 'salario': 4800},
    {'nome': 'Bruno', 'depto': 'TI', 'salario': 15000},
    {'nome': 'Karen', 'depto': 'Logística', 'salario': 3900},
    {'nome': 'Matheus', 'depto': 'TI', 'salario': 9500},
    {'nome': 'Talita', 'depto': 'Marketing', 'salario': 6100},
    {'nome': 'Douglas', 'depto': 'Vendas', 'salario': 5400},
    {'nome': 'Isabela', 'depto': 'RH', 'salario': 4600},
    {'nome': 'Roberto', 'depto': 'TI', 'salario': 17800},
    {'nome': 'Juliana', 'depto': 'Financeiro', 'salario': 7800},
    {'nome': 'Hamilton', 'depto': 'Logística', 'salario': 4100},
    {'nome': 'Lívia', 'depto': 'TI', 'salario': 8200},
    {'nome': 'Davi', 'depto': 'Marketing', 'salario': 6900},
    {'nome': 'Patrícia', 'depto': 'RH', 'salario': 5100},
    {'nome': 'Felipe', 'depto': 'TI', 'salario': 13400},
    {'nome': 'Camila', 'depto': 'Financeiro', 'salario': 6500},
    {'nome': 'Eduardo', 'depto': 'Logística', 'salario': 4400},
    {'nome': 'Igor', 'depto': 'TI', 'salario': 7600},
    {'nome': 'Amanda', 'depto': 'Vendas', 'salario': 5700},
    {'nome': 'Tiago', 'depto': 'TI', 'salario': 12100},
    {'nome': 'Beatriz', 'depto': 'Marketing', 'salario': 6100},
    {'nome': 'Otávio', 'depto': 'RH', 'salario': 4900},
    {'nome': 'Alice', 'depto': 'Financeiro', 'salario': 9100},
    {'nome': 'Henrique', 'depto': 'Logística', 'salario': 3600},
    {'nome': 'Sara', 'depto': 'TI', 'salario': 10100}
]

rh = [p['salario'] for p in funcionarios_rh if p['depto'] == "RH"]
media = sum(rh) / len(rh)
print(f"media de salario RH: {media}")