#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input("Digite um número: "))

divisores = 0
for divisor in range(1, numero):
    if numero % divisor == 0:
        divisores = divisores + 1

if divisores > 1:
  print("não é primo")
else:
  print("é primo")