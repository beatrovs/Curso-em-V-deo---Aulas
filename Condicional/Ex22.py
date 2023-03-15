#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 
# por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input("Quantos KM teve a viagem? "))
print("O KM de viagem foi de {} km/h".format(km))
km200 = km * 0.50
km2 = km * 0.45

if km <= 200:
    print("O valor a se pagar é de R$ {:.2f}".format(km200))
else:
    print("O valor a se pagar é de R$ {:.2f}".format(km2))

