# Faça um algoritmo que recebe uma lista de nomes ["Gabriel","Juliano","Anna","Marcos"] e conte a quantidade de nomes que tem a letra "a". Mostre no terminal com uma mensagem clara e intuitiva

nomes = ["Gabriel", "Juliano", "Anna", "Marcos"]
quantidade_com_a = 0
for nome in nomes:
    if "a" in nome:
        quantidade_com_a = quantidade_com_a + 1
print("Quantidade de nomes que possuem a letra 'a':", quantidade_com_a)
