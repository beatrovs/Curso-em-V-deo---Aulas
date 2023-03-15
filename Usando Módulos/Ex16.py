#Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo
#retângulo, calcule e mostre o comprimento da hipotenusa
#Existe uma função no math para calcular hipotenusa, que é a math.hypot


import math
co = float(input("Digite o valor de cateto oposto: ")) 
ca = float(input("Digite o valor de cateto adjacente: "))
hipo= math.hypot(co, ca)
print("A medida da hipotenusa é de {:.2f}".format(hipo))

