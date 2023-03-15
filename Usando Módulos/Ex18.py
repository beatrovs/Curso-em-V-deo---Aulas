#Um professor quer sortear a ordem de apresentação de trabalho 
#Faça um programa que leia o nome dos quatro estudantes e mostre a ordem sorteada

import random
n1 = str(input("Digite o nome do estudante: "))
n2 = str(input("Digite o nome do estudante: "))
n3 = str(input("Digite o nome do estudante: "))
n4 = str(input("Digite o nome do estudante: "))
estudantes = [n1, n2, n3, n4]
ordem = [1, 2, 3, 4]
print("Estudante escolhido foi ",random.choice(estudantes), random.choice(ordem))