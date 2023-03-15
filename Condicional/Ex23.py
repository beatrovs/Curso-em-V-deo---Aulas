#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Qual o ano que você escolheu? "))
print("O ano escolhido foi {}".format(ano))
bissexto = ano % 4

if bissexto == 0:
    print("O ano escolhido {} é considerado bissexto".format(ano))
else:
    print("O ano escolhido {} não é considerado bissexto".format(ano))