#Escreva um programa que leia o valor em metros e o exiba convertido em centimetros e milimetros

m = float(input("Quantos metros? "))
c = m*100
mm = m*1000
print("O tamanho é de {} m, {} c, {} mm ".format(m, c, mm))