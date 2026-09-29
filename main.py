#Exceções personalizadas
class ValorInferiorException(Exception):
    pass
class SaldoInsuficienteException(Exception):
    pass
class ContaInexistenteException(Exception):
    pass
class CpfduplicadoException(Exception):
    pass

#Classe Conta
class ContaBancaria:
    def __init__(self, numero_conta,cpf , titular, saldo=0):
        self.numero_conta = numero_conta
        self.cpf = cpf
        self.titular =  titular
        self.saldo = saldo

    def __str__(self):
        return f"Conta: {self.numero_conta}, Titular: {self.titular}, CPF: {self.cpf}, Saldo: R$ {self.saldo:.2f}"

    def depositar(self, valor):
        if valor <= 0:
            raise ValorInferiorException("O valor do depósito deve ser maior que zero.")

        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValorInferiorException("O valor do saque deve ser maior que zero.")
        if valor > self.saldo:
            raise SaldoInsuficienteException("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {self.saldo:.2f}")

    def transferir(self, valor , conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)
        print(f"Transferência de R$ {valor:.2f} realizada com sucesso. Novo saldo: R$ {self.saldo:.2f}")

#Classe Banco
class Banco:
    def __init__(self):
        self.contas = []
        self.contas_lista = [] #List
        self.cpf_set = set()  # Set
        self.contas_map = {} # Map (Dict)

    def cadastrar_conta(self, numero_conta, cpf, titular, saldo_inicial=0):
        if cpf in self.cpf_set:
            raise CpfduplicadoException(f"O CPF {cpf} já está cadastrado no sistema.")

        if numero_conta in self.contas_map:
            raise Exception(f"A conta {numero_conta} já existe.")

        nova_conta = ContaBancaria(numero_conta,cpf,titular,saldo_inicial)

        #Atualizando as três estruturas de dados
        self.contas_lista.append(nova_conta)
        self.cpf_set.add(cpf)
        self.contas_map[numero_conta] = nova_conta

        print(f"Conta {numero_conta} cadastrada com sucesso para o titular {titular}.")
        return nova_conta

    def buscar_conta(self,numero_conta):
        conta = self.contas_map.get(numero_conta)
        if not conta:
            raise ContaInexistenteException(f"A conta {numero_conta} não encontrada.")
        return conta

    def depositar(self,numero_conta, valor):
        conta = self.buscar_conta(numero_conta)
        conta.depositar(valor)

    def sacar(self,numero_conta, valor):
        conta = self.buscar_conta(numero_conta)
        conta.sacar(valor)
    def transferir(self, numero_conta_origem, numero_conta_destino, valor):
        conta_origem = self.buscar_conta(numero_conta_origem)
        conta_destino = self.buscar_conta(numero_conta_destino)
        conta_origem.transferir(valor, conta_destino)

if __name__ == "__main__":
    banco = Banco()

    # Cadastrando contas
    try:
        banco.cadastrar_conta("12345", "12345678901", "João Silva", 1000)
        banco.cadastrar_conta("67890", "98765432100", "Maria Oliveira", 500)
        banco.cadastrar_conta("54321", "11122233344", "Carlos Souza", 2000)
    except Exception as e:
        print(e)

    # Realizando operações
    try:
        banco.depositar("12345", 200)
        banco.sacar("67890", 100)
        banco.transferir("54321", "12345", 300)
    except Exception as e:
        print(e)

    # Exibindo informações das contas
    for conta in banco.contas_lista:
        print(conta)