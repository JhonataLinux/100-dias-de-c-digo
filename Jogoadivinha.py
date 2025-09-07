import random
print("jogo de adivinhacão")
print("tente adivinhar um numero de 1 a 100")
print("você tem 10 tentativas")
numero_secreto = random.randint(1, 20)
tentativas = 10
for tentativas in range(1, tentativas + 1):
    print(f"tentativa {tentativas} ")
    palpite = int(input("Digite o numero secreto: "))
    if palpite == numero_secreto:
        print(f"Parabens voce acertou em {tentativas} de {tentativas} tentativas")
        break
    elif palpite < numero_secreto:
        print("Tenta um numero MAIOR")
    elif palpite > numero_secreto:
        print("Tenta um numero MENOR")
print(f"Game Over! o numero secreto era {numero_secreto}")