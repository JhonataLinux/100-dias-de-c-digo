while True:
    n1 = int(input("Digite um numero "))
    f = 1
    for i in range(1, n1 + 1):
        f *= i
        print(f"o fatorial de {n1} é {f}")
    s = input("deseja encerrar digite 'S'ou 'N'").strip().upper()
    if s == 'S':
        break


