#Um professor quer sortear quatro estudantes para apagar um quadro
#Faça um programa que leia o nome dos quatro estudantes e escolha um


import random
n1 = str(input("Digite o nome do estudante: "))
n2 = str(input("Digite o nome do estudante: "))
n3 = str(input("Digite o nome do estudante: "))
n4 = str(input("Digite o nome do estudante: "))
estudantes = [n1, n2, n3, n4]
print("Estudante escolhido foi ",random.choice(estudantes))
