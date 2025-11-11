dir = []
esq = []
raiz = None
while True:
    print("*********** Arvore binaria************ ")
    print(" 1. digite um numero: ")
    print(" 2. lista raiz ")
    print(" 3. sair do programa digite ( -1): ")

    opcao = int(input())
    try:
        if opcao == 1:
            r = int(input("Digite um numero: "))
            if raiz == None:
                raiz = r
            elif r == raiz or r in dir or r in esq:
                print("numero ja existente")
            else:
                if r > raiz:
                    dir.append(r)
                else:
                     esq.append(r)
    except ValueError:
        print("digite apenas numeros")
        continue
    if opcao == 2:
       print("---- Arvore binaria ----")
       print(f"Raiz {raiz}")
       print(f"Direto ( > {raiz}: {dir}")
       print(f"Esquerda ( < {raiz}: {esq}")
       print(f"Total de Nó {len(dir) + len(esq) +1}")
       print("-----------------------------------")
    elif opcao == -1:
        break
