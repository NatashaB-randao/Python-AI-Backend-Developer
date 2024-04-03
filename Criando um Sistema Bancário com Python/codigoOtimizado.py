"""
Simulador de Operações Bancárias

Este programa implementa um simulador simples de operações bancárias, permitindo ao usuário realizar depósitos, saques, verificar o extrato da conta e sair do programa.

Funcionalidades:
- Cadastrar um usuário (cliente)
- Cadastrar uma conta bancária
- Depositar fundos na conta
- Sacar fundos da conta (com limites)
- Verificar o extrato da conta
- Sair do programa

Uso:
Execute o programa e siga as instruções exibidas no menu para realizar as operações desejadas.

Atributos:
- saldo (float): Saldo atual da conta.
- limite (float): Limite máximo permitido para saques.
- extrato (str): Histórico das transações realizadas na conta.
- numero_saques (int): Número de saques realizados.
- LIMITE_SAQUES (int): Limite máximo de saques permitidos.

"""

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Inicializa os atributos do usuário
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    numero_conta = 1

    def __init__(self, usuario):
        # Inicializa os atributos da conta corrente
        self.agencia = "0001"
        self.numero_conta = ContaCorrente.numero_conta
        ContaCorrente.numero_conta += 1
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        # Função para depositar dinheiro na conta
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

    def sacar(self, valor):
        # Função para sacar dinheiro da conta
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return False
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return False
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return False
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

    def mostrar_extrato(self):
        # Função para exibir o extrato da conta
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


def cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    # Função para cadastrar um novo usuário
    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Erro: CPF já cadastrado.")
            return None
    
    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    return novo_usuario

def cadastrar_conta(contas, usuario):
    # Função para criar uma nova conta corrente
    nova_conta = ContaCorrente(usuario)
    contas.append(nova_conta)
    return nova_conta

def main():
    # Função principal do programa
    usuarios = []
    contas = []

    while True:
        # Menu principal
        print("\n[1] Cadastrar Usuário")
        print("[2] Criar Conta Corrente")
        print("[3] Acessar Conta")
        print("[4] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Opção para cadastrar um novo usuário
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, número - bairro - cidade/estado): ")
            novo_usuario = cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco)
            if novo_usuario:
                print("Usuário cadastrado com sucesso.")
            else:
                print("Falha ao cadastrar usuário.")
        
        elif opcao == "2":
            # Opção para criar uma nova conta corrente
            cpf = input("CPF do titular da conta: ")
            usuario = None
            for u in usuarios:
                if u.cpf == cpf:
                    usuario = u
                    break
            if usuario:
                nova_conta = cadastrar_conta(contas, usuario)
                print(f"Conta criada com sucesso. Número da conta: {nova_conta.numero_conta}")
            else:
                print("Usuário não encontrado.")
        
        elif opcao == "3":
            # Opção para acessar uma conta corrente existente
            num_conta = input("Digite o número da conta: ")
            for conta in contas:
                if str(conta.numero_conta) == num_conta:
                    operar_conta(conta)
                    break
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            # Opção para sair do programa
            print("Saindo...")
            break

        else:
            # Opção inválida
            print("Opção inválida. Tente novamente.")

def operar_conta(conta):
    # Função para operar uma conta corrente
    while True:
        # Menu de operações da conta corrente
        print("\n[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Opção para depositar dinheiro na conta
            valor = float(input("Informe o valor do depósito: "))
            if conta.depositar(valor):
                print("Depósito realizado com sucesso.")
        
        elif opcao == "2":
            # Opção para sacar dinheiro da conta
            valor = float(input("Informe o valor do saque: "))
            if conta.sacar(valor):
                print("Saque realizado com sucesso.")
        
        elif opcao == "3":
            # Opção para exibir o extrato da conta
            conta.mostrar_extrato()
        
        elif opcao == "4":
            # Opção para voltar ao menu anterior
            print("Voltando ao menu anterior...")
            break
        
        else:
            # Opção inválida
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    # Executa a função principal quando o programa é executado diretamente
    main()



# Neste código, reorganizamos as funcionalidades em classes `Usuario` e `ContaCorrente`, bem como funções auxiliares para cadastrar usuários, criar contas correntes e operar contas. Agora o programa segue uma estrutura mais organizada e modular, facilitando a manutenção e expansão futura.