#Escreva um programa que leia a velocidade de um carro, se ultrapassar 80km/h, mostre a 
#mensagem que foi multado. A multa vai custar R$7,00 para cada km por hora

vel = int(input("Qual a sua velocidade? "))
print("A velocidade foi de {}".format(vel))
multa = (vel-80) * 7.00

if vel >80.0:
    print("Você ultrapassou o limite de velocidade, pague R$ {:.2f}".format(multa))
else:
    print("Você não pagará a multa!")