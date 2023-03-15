#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Qual o valor da casa? "))
salário = float(input("Qual o valor do salário? "))
anos = int(input("Quantos anos para pagar o valor da casa?"))
prestação = casa / (anos * 12)
mínimo = (salário * 30 / 1000)
print("Para pagar uma casa de R${:.2f} em anos {}, a prestação será de R${:.2f}".format(casa, anos, prestação))
if prestação <= mínimo:
    print("Empréstimo autorizado!")
else:
    print("Empréstimo não autorizado!")