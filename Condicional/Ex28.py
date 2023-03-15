#Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
ano = int(input("Escreva o ano do seu nascimento: "))
idade = atual - ano
print("Quem nasceu em {} tem {} anos em {}".format(ano, idade, atual))


if idade == 18:
    print("Parabéns! Você tem ou vai fazer 18 anos, pode se alistar!")
elif idade < 18:
    diferença = (18 - idade)
    print("Faltam {} anos para você se alistar!".format(diferença))
elif idade > 18:
    diferença = (idade - 18)
    print("Você já deveria ter se alistado há {} anos.".format(diferença))
