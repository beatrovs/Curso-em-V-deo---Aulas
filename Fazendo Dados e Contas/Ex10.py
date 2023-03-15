#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares
#ela pode comprar. US$1,00=R$3,27

carteira = float(input("Quantos reais você tem? "))
cotacao = carteira / 3.27
print("Poderá comprar", cotacao)