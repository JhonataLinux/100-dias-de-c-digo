class ContaBancaria:
    def __init__(self,titular,numero,saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositor(self,saldo):
        if self.saldo > 0 :
            self.saldo += saldo
            print(f"Deposito realizado com sucesso! {self.saldo}")
        else:
            print("Valor de depósito inválido.")
    def secar(self,saldo):
        if 0 <= saldo <= self.saldo:
            self.saldo -= saldo
            print(f"saque realizado com sucesso! saque de $ {self.saldo}!")
        else:
            print("saldo insuficiente.")
    def exibir_dasos(self):
        print(f"titular: {self.titular}")
        print(f"numero: {self.numero}")
        print(f"saldo: {self.saldo}")

conta1 = ContaBancaria(titular="Jhontan",numero="25435")
conta1.exibir_dasos()
conta1.saldo = 2000
conta1.depositor(200)
conta1.secar(10)
conta1.exibir_dasos()