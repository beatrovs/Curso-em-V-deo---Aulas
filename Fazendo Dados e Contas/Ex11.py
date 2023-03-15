#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input("Quanto é o valor do produto? R$ "))
desconto = produto - (produto * 5 /100)
print("O preço antigo do produto era de R$ {} e com desconto ficou R$ {}".format(produto, desconto))