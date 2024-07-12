from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Atenção!".center(50, "."))
            print("\n⛔...Você não tem saldo suficiente.Operação falhou! ⛔")
            print(" ".center(50, "."))

        elif valor > 0:
            self._saldo -= valor
            print("Operação de saque:!".center(50, "."))
            print("\n✅ Saque realizado com sucesso!")
            print(" ".center(50, "."))
            return True

        else:
            print("Atenção!".center(50, "."))
            print("\n⛔...Valor inválido. Operação falhou! ⛔")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Operação de saque:!".center(50, "."))
            print("\n✅ Saque realizado com sucesso!")
        else:
            print("Atenção!".center(50, "."))
            print("\n⛔...Valor inválido. Operação falhou! ⛔")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        Texto_Atencao = "ATENÇÃO!"
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print(Texto_Atencao.center(50, "."))
            print("\n⛔ Operação falhou! O valor do saque excede o limite. ⛔")

        elif excedeu_saques:
            print(Texto_Atencao.center(50, "."))
            print("\n⛔ Operação falhou! Limite de saque excedido. ⛔")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(),            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """
..........BEM VINDO AO SEU BANCO..........

Escolha uma das as opções abaixo;

[1] 💸 Depositar
[2] 💰 Sacar
[3] 🧾 Extrato
[4] 👤 Criar Novo Usuário
[5] 📑 Criar Nova Conta
[6] 🏸 Consultar Usuários
[0] ❌ Sair

...........ESCOLHA UMA DAS OPÇÕES..........
>>>"""
    return input(menu)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n⛔ Cliente não possui conta! ⛔")
        return

    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n⛔ Cliente não encontrado! ⛔")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    Texto_Atencao = "ATENÇão!"
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
       print(Texto_Atencao.center(50, "."))
       print("\n.............Usuário não encontrado............")
       print("\n.........Por favor, cadastre o usuario!........")
       print("\n⛔............Operação cancelada!...........⛔")
       return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
       print("\n.............Usuário não encontrado............")
       print("\n.........Por favor, cadastre o usuario!........")
       print("\n⛔............Operação cancelada!...........⛔")
       return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    print("EXTRATO".center(50, "."))
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print(".".center(50, "."))

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n⛔ Já existe cliente com esse CPF! ⛔")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n ✅ Cliente criado com sucesso! ")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n⛔ Cliente não encontrado, fluxo de criação de conta encerrado! ⛔")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n ✅ Conta criada com sucesso!".center(50, "."))

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print((conta))

def op_invalida():
    Texto_Ivalido = "⛔VALOR INVÁLIDO!⛔"
    Texto_Atencao = "ATENÇÃO!"
    print(Texto_Atencao.center(50, "."))
    print(Texto_Ivalido.center(50, "."))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_cliente(clientes)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            op_invalida

main()