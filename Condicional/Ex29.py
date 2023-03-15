#Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite a sua nota: "))
nota2= float(input("Digite a sua nota: "))
nota3 = float(input("Digite a sua nota: "))
nota4 = float(input("Digite a sua nota: "))
notas = (nota1 + nota2 + nota3 + nota4) / 4

if notas >= 7:
    print("A sua nota foi {} e está APROVADO! Parabéns!".format(notas))
elif 7 > notas >= 5:
    print("A sua nota foi {} e está em RECUPERAÇÃO! Vamos estudar!".format(notas))
elif notas < 5.0:
    print("A sua nota foi {} e você está REPROVADO. Não fique triste, vamos estudar juntos!".format(notas))


