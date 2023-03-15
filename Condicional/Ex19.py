#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5, peça
#para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
computador = randint(0, 5)
jogador = int(input("Qual número inteiro você pensou? "))

if jogador == computador:
    print("Parabéns! Você acertou o número.")
else:
    print("Não foi dessa vez, o computador pensou no número {} e você no {}".format(computador, jogador))