
while True:
    print("*******************************")
    print("_______cadastro______")
    print("1. digite seu nome")
    print("2. digite sua idade")
    print("3. sair do programa ")
    print("*******************************")
    opcao = input("Digite a opção")
    if opcao not in ["1", "2", "3"]:
        print("opão invalida!")
    if opcao == '1':
        nome = input("Digite seu nome :  ")
        palavra_min = nome.lower()

        total_vogais = 0
        for letras in palavra_min:
            if letras in 'aeiou':
               total_vogais += 1
        print(f"seu nome: {nome}")
        print(f"O seu nome contém {total_vogais} vogais.")

    if opcao == '2':
        idade = int(input("Digite sua idade: \n "))
        soma = idade - 2025
        print(f"O ano de nascimento: {soma}")
        if soma >= 50:
            print(f"Uma pessoa de 50 anos é considerada meia-idade")
        elif soma >= 30:
            print("Os 30 anos são considerados uma transição para o início da fase adulta madura")
        elif soma >= 20:
            print("Uma pessoa de 20 anos é considerada um jovem adulto")
        elif soma <= 19:
            print("Uma pessoa de 18 anos é considerada adulta e maior de idade")
        else:
            print("é considerada criança pela legislação brasileira")
    if opcao == '3':
        break










