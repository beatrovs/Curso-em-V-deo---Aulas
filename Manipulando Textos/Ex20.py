#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#Por exemplo, 1834. Unidade: 4, Dezena: 3, Centena: 8, Milhar: 1

num = int(input("Digite um número: "))
n = str(num)
print('Analisando um número {}'.format(num))
print("Unidade: {}".format(n[3]))
print("Dezena: {}".format(n[2]))
print("Centena: {}".format(n[1]))
print("Milhar: {}".format(n[0]))