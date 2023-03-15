#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada

num = int(input("Digite um número "))
dobro = num * 2
triplo = num * 3
raiz = math.pow(num)
print("O dobro de num é {}, o triplo é {} e a raiz quadrada é {}".format(dobro, triplo, raiz))