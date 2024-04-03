"""
Simulador de Operações Bancárias

Este programa implementa um simulador simples de operações bancárias, permitindo ao usuário realizar depósitos, saques, verificar o extrato da conta e sair do programa.

Funcionalidades:
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

# Menu de opções para o usuário
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    # Solicitação da opção do usuário
    opcao = input(menu)

    # Opção: Depositar
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção: Sacar
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção: Extrato
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Opção: Sair
    elif opcao == "q":
        break

    # Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


# Esta documentação fornece uma descrição geral do programa, incluindo suas funcionalidades, uso e atributos. Ela segue o padrão de docstrings Python, o que facilita a compreensão do código e seu uso por outros desenvolvedores.