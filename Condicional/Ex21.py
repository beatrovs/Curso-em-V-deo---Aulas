#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Escolha um número: "))
resultado = num % 2

if resultado == 0:
    print("O número escolhido foi {} e é par".format(num))
else:
    print("O número escolhido foi {} e é impar".format(num))