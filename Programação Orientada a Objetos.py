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

class Resumo_aplicado(ContaBancaria):
    def __init__(self, titular, saldo_inicial = 0.0, valor = 0.0 ,resumo=""):
        super().__init__(titular, saldo_inicial)
        self.valor = valor
        self.resumo = resumo
        self.saldo_inicial = saldo_inicial

    def resumo_total(self):
        print(f'Conta bancaria {self.titular} '
              f'Saldo inicial {self.saldo_inicial} '
              f'Saldo atual {self.saldo} '
              f'Obsevação {self.resumo if self.resumo else 'Nenhum'}!')



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

class Debitar(ContaCorrente):
    def __init__(self,titular,saldo_inicial = 0.0, limite_inicial = 100.0, desconto = 12.90):
        super().__init__(titular,saldo_inicial)
        self.limite = float (limite_inicial)
        self.desconto = float (desconto)

    def Aplicar_desconto(self):
        if self.saldo > 0:
            self.saldo -= self.desconto
            print(f"Foi descontado {self.desconto} da conta do titular {self.titular}"
                  f" novo saldo {self.saldo}")
        else:
            print("Saldo insuficiente para aplicar desconto!")

class ResumoContaCorrente(ContaCorrente):
    def __init__(self,titular,saldo_inicial = 0.0, limite_inicial = 100.0, resumo = "", valor = 0.0,desconto = 12.90):
        super().__init__(titular,saldo_inicial,desconto)
        self.limite = float (limite_inicial)
        self.desconto = float (desconto)
        self.resumo = resumo
        self.valor = valor

    def resumo_total(self):
        print(f'Conta corre {self.titular} '
              f'limite inicial {self.limite} '
              f'saldo atual {self.saldo} '
              f'desconto {self.desconto} '
              f'Resumido {self.resumo if self.resumo else 'Nenhum'}!')


class ContaPoupanca(ContaBancaria):
    def __init__(self,titular, saldo_inicial = 0.0, taxa_rendimento = 0.05):
        super().__init__(titular,saldo_inicial)
        self.rendimento = float (taxa_rendimento)

    def render_juros(self):
        if self.saldo > 0:
            self.saldo += self.saldo * self.rendimento
            print(f"Sua conta esta rendedo ao taxa de  $ {self.rendimento} ao mes ")

class ResumoContaPoupanca(ContaPoupanca):
    def __init__(self,titular, saldo_inicial = 0.0, taxa_rendimento = 0.05, valor = 0.0,resumo = ""):
        super(). __init__(titular,saldo_inicial,taxa_rendimento)
        self.valor = valor
        self.resumo = resumo
        self.saldo_inicial = saldo_inicial
        self.taxa_rendimento = taxa_rendimento

    def resumo_total(self):
        print(f'Conta poupanca {self.titular} '
              f'saldo inicial {self.saldo_inicial} '
              f'saldo atual {self.saldo} '
              f'rendimento {self.taxa_rendimento} '
              f'Resumido {self.resumo if self.resumo else 'Nenhum'}!')

class Isenta(ContaPoupanca):
    def __init__(self,titular, saldo_inicial = 0.0, taxa_rendimento = 0.05, ajuste = 5.00):
        super().__init__(titular,saldo_inicial,taxa_rendimento)
        self.ajuste = float (ajuste)

    def aplicar_isenta(self):
        if self.saldo < 999:
            self.saldo -= self.ajuste
            print(f"houve um desconto de {self.ajuste} na sua conta {self.titular}"
                  f" novo saldo {self.saldo}")
        else:
            print("nao houve desconto em sua conta!")




conta1 = ContaBancaria ("Jhonata", 500)
conta2 = ContaCorrente ("Isabela",800, limite_inicial=300)
conta3 = ContaPoupanca ("Jose ", 100, taxa_rendimento=0.05)
conta4 = Debitar("Juliana",900, desconto=12.90)
conta5 = Isenta("almir", 940, ajuste=5.00)

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

conta4.extrato()
conta4.depositar(100)
conta4.Aplicar_desconto()

conta5.extrato()
conta5.depositar(40)
conta5.aplicar_isenta()

conta6 = Resumo_aplicado("Carla", 200, 100, resumo="Conta criada para guardar salário")


conta6.depositar(300)
conta6.resumo_total()

conta7 = Resumo_aplicado("Kayk", 100,200, resumo="Conta criada para guarda dinheiro para uma viajem")
conta7.depositar(100)
conta7.resumo_total()


c1 = ResumoContaPoupanca("Jhonatan", 1000, 0.08, 500, "Aplicação mensal")
c1.resumo_total()
