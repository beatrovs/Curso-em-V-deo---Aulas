#Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente
#Caso de nomes completos maior que 3

n= str(input("Digite o seu nome completo: ")).strip()
nome = n.split()
print("Nome: {}".format(nome[0]))
print("Sobrenome: {}".format(nome[len(nome)-1]))