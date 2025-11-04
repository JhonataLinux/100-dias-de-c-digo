usuarios = []


def validar_idade(idade):
    try:
        idade_int = int(idade)
        if 18 <= idade_int <= 85:
            return True
        else:
            print("Idade deve estar entre 18 e 85 anos.")
            return False
    except ValueError:
        print("Idade deve ser um número.")
        return False


def valida_email(email):
    if len(email) < 5:
        print("E-mail deve ter pelo menos 5 caracteres.")
        return False
    if '@' not in email or '.' not in email:
        print("O e-mail deve conter '@' e '.'")
        return False
    if ' ' in email:  # CORREÇÃO: 'not in' -> 'in'
        print("E-mail não pode conter espaços.")
        return False
    return True


def valida_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF deve conter exatamente 11 números.")
        return False
    if cpf == cpf[0] * 11:
        print("O CPF não pode ter todos os dígitos iguais.")
        return False
    for usuario in usuarios:  # CORREÇÃO: 'usuarios' -> 'usuario' no loop
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return False
    return True


def cadastra_usuario():
    print("\n--- NOVO CADASTRO ---")
    nome = input("Nome: ")

    idade = input("Idade: ")
    if not validar_idade(idade):
        return

    email = input("E-mail: ")
    if not valida_email(email):
        return

    cpf = input("CPF (apenas números): ")
    if not valida_cpf(cpf):
        return

    novo_usuario = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
        'email': email,
    }
    usuarios.append(novo_usuario)
    print("✅ Usuário cadastrado com sucesso!")


def lista_usuarios():
    if not usuarios:  # CORREÇÃO: variável global corrigida
        print("Nenhum usuário cadastrado.")
        return

    print("\n--- LISTA DE USUÁRIOS ---")
    for i, usuario in enumerate(usuarios, start=1):  # CORREÇÃO: variável global
        print(f"Usuário {i}:")
        print(f"  Nome: {usuario['nome']}")
        print(f"  Idade: {usuario['idade']}")
        print(f"  CPF: {usuario['cpf']}")
        print(f"  E-mail: {usuario['email']}")
        print()


def buscar_usuario():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    cpf_buscar = input("Digite o CPF para buscar: ")

    for usuario in usuarios:  # CORREÇÃO: 'usuarios' -> 'usuario' no loop
        if usuario['cpf'] == cpf_buscar:
            print("\n✅ USUÁRIO ENCONTRADO:")
            print(f"  Nome: {usuario['nome']}")
            print(f"  Idade: {usuario['idade']}")
            print(f"  CPF: {usuario['cpf']}")
            print(f"  E-mail: {usuario['email']}")
            return

    print("❌ Usuário não encontrado.")


def menu_principal():
    while True:
        print("\n" + "=" * 50)
        print("🏢 SISTEMA DE CADASTRO DE USUÁRIOS")
        print("=" * 50)
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Buscar por CPF")
        print("4 - Sair")
        print("=" * 50)

        opcao = input("Digite a opção desejada: ").strip()

        if opcao == "1":
            cadastra_usuario()
        elif opcao == "2":
            lista_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            print("\n👋 Saindo do sistema... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()