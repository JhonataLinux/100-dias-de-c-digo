from typing import Dict, List


# Classes e Herança 

class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str, email: str):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    def __repr__(self) -> str:
        return f"Cliente(nome={self.nome}, cpf={self.cpf}, telefone={self.telefone}, email={self.email})"


class Servico:
    def __init__(self, cpf: str, descricao: str, preco: float, status: str = "aberto"):
        self.cpf = cpf
        self.descricao = descricao
        self.preco = preco
        self.status = status

    def __repr__(self) -> str:
        return f"Servico(cpf={self.cpf}, descricao={self.descricao}, preco={self.preco}, status={self.status})"


class ItemEstoque:
    def __init__(self, nome_peca: str, quantidade: int = 0, preco_custo: float = 0.0):
        self.nome_peca = nome_peca
        self.quantidade = quantidade
        self.preco_custo = preco_custo

    def __repr__(self) -> str:
        return f"ItemEstoque(peca={self.nome_peca}, qtd={self.quantidade}, preco_custo={self.preco_custo})"



# "Banco" em memória

clientes: Dict[str, Cliente] = {}
servicos: Dict[str, List[Servico]] = {}
estoque: Dict[str, ItemEstoque] = {}


# Ajudante - aceitar somente digito

def _somente_digitos(texto: str) -> str:
    return "".join(c for c in texto if c.isdigit())

def _cpf_valido(cpf: str) -> bool:
    cpf = _somente_digitos(cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    soma = sum(int(d) * p for d, p in zip(cpf[:9], range(10, 1, -1)))
    dv1 = (soma * 10) % 11
    dv1 = 0 if dv1 == 10 else dv1
    soma = sum(int(d) * p for d, p in zip(cpf[:9] + str(dv1), range(11, 1, -1)))
    dv2 = (soma * 10) % 11
    dv2 = 0 if dv2 == 10 else dv2
    return cpf[-2:] == f"{dv1}{dv2}"


# Funções - Cliente

def cadastrar_cliente() -> None:
    cpf_input = input("CPF: ").strip()
    cpf = _somente_digitos(cpf_input)

    if not _cpf_valido(cpf):
        print("CPF inválido.")
        return

    if cpf in clientes:
        print("CPF já cadastrado.")
        return

    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    clientes[cpf] = Cliente(nome, cpf, telefone, email)
    print(" Cliente cadastrado com sucesso!")


def listar_clientes() -> None:
    if not clientes:
        print("Não há clientes cadastrados.")
        return
    for c in clientes.values():
        print(c)


def buscar_cliente() -> None:
    cpf_input = input("CPF para buscar: ").strip()
    cpf = _somente_digitos(cpf_input)
    cli = clientes.get(cpf)
    print(cli if cli else "Cliente não encontrado.")


# Funções - Serviço

def cadastrar_servico() -> None:
    cpf_input = input("CPF do cliente: ").strip()
    cpf = _somente_digitos(cpf_input)
    if cpf not in clientes:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return

    descricao = input("Descrição do serviço: ").strip()
    preco_str = input("Preço do serviço (use vírgula ou ponto): ").strip()
    try:
        preco = float(preco_str.replace(",", "."))
    except ValueError:
        print("Preço inválido.")
        return

    status = (input("Status (aberto/em andamento/finalizado/entregue) [aberto]: ").strip()
              or "aberto")

    serv = Servico(cpf, descricao, preco, status)
    servicos.setdefault(cpf, []).append(serv)
    print(" Serviço cadastrado!")


def listar_servicos() -> None:
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    for cpf, lista in servicos.items():
        dono = clientes.get(cpf).nome if cpf in clientes else "(desconhecido)"
        print(f"\nCPF: {cpf} - {dono} | {len(lista)} serviço(s)")
        for s in lista:
            print("  ", s)


def buscar_servicos_por_cpf() -> None:
    cpf_input = input("CPF para listar serviços: ").strip()
    cpf = _somente_digitos(cpf_input)
    lista = servicos.get(cpf)
    if not lista:
        print("Nenhum serviço encontrado para este CPF.")
        return
    for s in lista:
        print(s)


# Funções - Estoque

def cadastrar_peca() -> None:
    nome = input("Nome da peça: ").strip()
    if not nome:
        print("Nome inválido.")
        return

    qtd_str = input("Quantidade: ").strip()
    custo_str = input("Preço de custo (use vírgula ou ponto): ").strip()
    try:
        qtd = int(qtd_str)
        custo = float(custo_str.replace(",", "."))
    except ValueError:
        print("Quantidade ou preço inválidos.")
        return

    estoque[nome] = ItemEstoque(nome, qtd, custo)
    print(" Peça cadastrada no estoque!")


def listar_estoque() -> None:
    if not estoque:
        print("Estoque vazio.")
        return
    for item in estoque.values():
        print(item)


def baixar_peca() -> None:
    nome = input("Nome da peça para baixar: ").strip()
    item = estoque.get(nome)
    if not item:
        print("Peça não encontrada no estoque.")
        return

    qtd_str = input("Quantidade a baixar: ").strip()
    try:
        qtd = int(qtd_str)
    except ValueError:
        print("Quantidade inválida.")
        return

    if qtd <= 0:
        print("Quantidade deve ser maior que zero.")
        return
    if qtd > item.quantidade:
        print(f"Quantidade indisponível em estoque (disponível: {item.quantidade}).")
        return

    item.quantidade -= qtd
    print(f" Baixa realizada. Novo saldo de '{nome}': {item.quantidade}")


# Relatórios

def relatoria_servico() -> None:
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    print("\n====> RELATÓRIO DE SERVIÇOS <====")
    for cpf, lista in servicos.items():
        dono = clientes.get(cpf).nome if cpf in clientes else "(desconhecido)"
        print(f"\nCliente: {dono} | CPF: {cpf}")
        for s in lista:
            print(f" - {s.descricao} | R${s.preco:.2f} | Status: {s.status}")

def relatorio_estoque() -> None:
    if not estoque:
        print("Estoque vazio.")
        return
    print("\n==== RELATÓRIO DE ESTOQUE ====")
    baixo_estoque = []
    for item in estoque.values():
        print(f" - {item.nome_peca}: {item.quantidade} un. | Custo: R${item.preco_custo:.2f}")
        if item.quantidade <= 5:
            baixo_estoque.append(item)
    if baixo_estoque:
        print("\n* Itens com pouca unidade (<= 5):")
        for it in baixo_estoque:
            print(f"   • {it.nome_peca}: {it.quantidade} un.")


# Menu

def menu() -> None:
    opcoes = {
        "1":  ("Cadastrar cliente", cadastrar_cliente),
        "2":  ("Listar clientes", listar_clientes),
        "3":  ("Buscar cliente", buscar_cliente),
        "4":  ("Cadastrar serviço", cadastrar_servico),
        "5":  ("Listar serviços (todos)", listar_servicos),
        "6":  ("Buscar serviços por CPF", buscar_servicos_por_cpf),
        "7":  ("Cadastrar peça no estoque", cadastrar_peca),
        "8":  ("Listar estoque", listar_estoque),
        "9":  ("Baixar peça do estoque", baixar_peca),
        "10": ("Relatório de serviços e status", relatoria_servico),
        "11": ("Relatório do estoque (quantidades)", relatorio_estoque),
        "0":  ("Sair", None),

        }
    print("TI Soluções em Informática")
    
    while True:
        print("\n------> MENU <------")
        for k, (nome, _) in opcoes.items():
            print(f"{k} - {nome}")
        escolha = input("Escolha: ").strip()

        if escolha == "0":
            print("Até mais!")
            break

        acao = opcoes.get(escolha)
        if not acao:
            print("Opção inválida.")
            continue

        _, func = acao
        func()

if __name__ == "__main__":
    menu()

