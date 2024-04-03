# Desafio
# Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário inserir até três equipamentos.

# Entrada
# O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

# Saída
# Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.

# Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# Loop para solicitar os itens ao usuário:
for i in range(3):
    # Solicita o item e armazena na variável "item":
    item = input().strip()
    # Adiciona o item à lista "itens":
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")

