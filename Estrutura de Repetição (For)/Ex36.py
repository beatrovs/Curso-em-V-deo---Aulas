#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Digite um valor: "))
razao = int(input("Digite um valor: "))
decimo = primeiro + (10 - 1) * razao
for termo in range(primeiro, decimo + razao, razao):
    print("{}".format(termo, end=">"))


