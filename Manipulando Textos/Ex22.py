#Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "Silva" no sobrenome

nome = str(input("Qual o seu nome completo? ")).strip()
print("Seu nome tem Silva? {}".format("Silva" in nome))