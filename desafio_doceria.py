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

print("  Bem-vindo ao Cadastro da Doceria!  ")

clientes={}
import os 

while True:
    valor_receber_nome = input("Qual o seu nome?")
    if valor_receber_nome == "sair":
        print("Até breve")
        break 
    valor_receber_telefone = input("Qual o seu telefone?")
    valor_receber_email = input("Qual o seu email?")
    print("Obrigado pelo o cadastro")


vencedor = random.choice(valor_receber_nome)
print ("o vencedor é " + vencedor)


