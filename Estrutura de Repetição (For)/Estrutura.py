'''
for oi in range(1,6): #a estrutura que conta, não vai repetir 6x, mas 5x, caso queira repetir 6x, colocar 7x
    print(oi)
 '''   

'''
for oi in range (0, 7, 2): #contou de 0 até 7, pulando os números de 2 em 2.
    print(oi)
'''

'''
n = int(input("Digite um número: "))
for c in range (0, n):
    print(c)
'''

'''
for c in range (0, 3): #vai pedir digite um número 3x, pela quantidade.
    n = int(input("Digite um número: "))
'''

'''
s = 0
for c in range (0,4):
    n = int(input("Digite o valor: "))
    s +=n
print("O somatório de todos os números são {}".format(s))
'''
'''

i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for numero in range (i, f+1, p):
    print(numero)
    # para pular os números, colocar um inicio e um fim.
'''