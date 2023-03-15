
# Faça um programa que calcule a soma entre todos 
# os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        print(n, end=' ')
        soma = soma + n
print("A soma de todos os números é {}".format(soma))
