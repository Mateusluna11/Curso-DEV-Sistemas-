#4 - Crie uma classe para implementar uma conta corrente.

class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
        print("Nome do correntista alterado com sucesso.")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Insira um valor positivo.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

conta = ContaCorrente(numero_conta="12345", nome_correntista="João da Silva", saldo=1000.00)

print(f"Saldo inicial: R${conta.saldo}")

conta.deposito(500.00)
conta.saque(200.00)

print(f"Saldo atual: R${conta.saldo}")

conta.alterar_nome("João Oliveira")
