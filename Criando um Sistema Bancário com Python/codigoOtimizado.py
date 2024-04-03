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

# Função para cadastrar um usuário
def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    return {"nome": nome, "cpf": cpf}

# Função para cadastrar uma conta bancária
def cadastrar_conta():
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    limite_saque = float(input("Digite o limite de saque da conta: "))
    return {"saldo": saldo_inicial, "limite": limite_saque, "extrato": "", "numero_saques": 0}

# Função para realizar um depósito
def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para realizar um saque
def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

# Função para exibir o extrato da conta
def extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

# Função principal
def main():
    cliente = cadastrar_usuario()
    conta = cadastrar_conta()

    while True:
        # Menu de opções para o usuário
        menu = """

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """

        # Solicitação da opção do usuário
        opcao = input(menu)

        # Opção: Depositar
        if opcao == "d":
            depositar(conta)

        # Opção: Sacar
        elif opcao == "s":
            sacar(conta)

        # Opção: Extrato
        elif opcao == "e":
            extrato(conta)

        # Opção: Sair
        elif opcao == "q":
            break

        # Opção inválida
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()


# Neste código, as funcionalidades foram divididas em funções separadas para cada operação bancária (cadastrar usuário, cadastrar conta, depositar, sacar, extrato). Isso torna o código mais organizado, legível e reutilizável. Além disso, a função `main()` foi criada para controlar a execução principal do programa.