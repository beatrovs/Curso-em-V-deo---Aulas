#Crie um programa que leia o nome completo da pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras tem no total
#Quantas letras tem no primeiro nome

nome = str(input("Digite o seu nome completo: ")).strip() #serve para eliminar os espaços
print("Analisando o seu nome... ")
print(nome.upper())
print(nome.lower())
print(len(nome)- nome.count(" ")) #não conta os espaços que sobraram
print(nome.find(" "))
