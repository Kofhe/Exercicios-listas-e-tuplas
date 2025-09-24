# Desafio em dupla

# - Doceria, você foi contratado para desenvolver um sistema para uma doceria
# - O programa deverá rodar em looping pedindo informações do tipo, nome, telefone e email.
# - O programa deverá quebrar o looping de repetição se o nome digitado for "sair"
# - No final do programa o algoritmo irá sortear um cliente aleatoriamente para receber um brinde de dia das Crianças

# Critério de Avaliação 
# - Os nomes terão que ser armazenados e organizados de maneira clara e legível
# - O código não pode quebrar
# - tente deixar visualmente bonito (capricha ai )

import random

print("Bem-vindo ao Cadastro da Doceria!")

clientes = {}

while True:
    nome = input("Nome (ou 'sair'): ")
    if nome.lower() == "sair":
        break
    telefone = input("Telefone: ")
    email = input("Email: ")
    clientes[nome] = (telefone, email)

if clientes:
    vencedor = random.choice(list(clientes))
    print(f"Vencedor: {vencedor}")
    for nome, (telefone, email) in clientes.items():
        print(f"{nome}: {telefone}, {email}")
else:
    print("Nenhum cliente.")

============================================
Correção
============================================

import random

print("="*40)
print("Bem-vindo ao Cadastro da Doceria!".center(40))
print("="*40)

clientes = {}

while True:
    nome = input("Nome (ou 'sair'): ")
    if nome.lower() == "sair":
        break
    telefone = input("Telefone: ")
    email = input("Email: ")
    clientes[nome] = (telefone, email)
    clientes.append(clientes)
    print("\033[31mCliente Adicionado com Sucesso!\033[m")

    cliente_sorteado =choice(clientes) # choice escolhe aleatoriamente dentre da lista de valores
    print(f'Parabéns {cliente_sorteado[nome]} Você foi sorteado!')



