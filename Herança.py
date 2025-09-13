class ContaBancaria:
    def __init__(self, titular,saldo_inicial = 0.0):
        self.titular = titular
        self.saldo = float (saldo_inicial)

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito realizado com sucesso! {self.saldo}")

    def sacar(self, valor):
        if valor < 0:
            print("saque realizado com sucesso!")
        if valor > self.saldo:
            print("saldo insuficiente!")


    def extrato(self):
        print(f"Extrato realizado com sucesso! {self.titular} $ {self.saldo}")



class ContaCorrente(ContaBancaria):
    def __init__(self,titular,saldo_inicial = 0.0, limite_inicial = 100.0):
        super().__init__(titular,saldo_inicial)
        self.limite = float (limite_inicial)

    def sacar (self, valor):
        if valor < 0:
            print("Saque deve ser positivo!")
        if valor > self.saldo + self.limite:
            print("Limite de cheque especial excedido")
            self.saldo -= valor
    def extrato(self):
        print(f"Limite de cheque especial excedido:{self.titular} $ {self.limite}")

class ContaPoupanca(ContaBancaria):
    def __init__(self,titular, saldo_inicial = 0.0, taxa_rendimento = 0.12):
        super().__init__(titular,saldo_inicial)
        self.rendimento = float (taxa_rendimento)

    def render_juros(self):
        if self.saldo > 0:
            self.saldo += self.saldo * self.rendimento
            print(f"rendimento: $ {self.rendimento} ao mes ")

    def valor_juros(self):
        if self.saldo > 0:
            self.saldo - self.rendimento
            print(f"rendimento: $ {self.rendimento} ao mes ")

conta1 = ContaBancaria ("Jhonata", 500)
conta2 = ContaCorrente ("Isabela",800, limite_inicial=300)
conta3 = ContaPoupanca ("Jose ", 150, taxa_rendimento=0.12)

conta1.depositar(100)
conta1.sacar(800)
conta1.extrato()

conta2.depositar(280)
conta2.extrato()
conta2.sacar(1250)

conta3.depositar(500)
conta3.extrato()
conta3.render_juros()
conta3.extrato()
conta3.valor_juros()
