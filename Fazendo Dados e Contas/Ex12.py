#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário
# com 15% de aumento.

salario = float(input("Qual o seu salário? R$ "))
aumento = salario + (salario *15 / 100)
print("O seu antigo salário era de R$ {} e com o desconto ficou R$ {}".format(salario, aumento))
