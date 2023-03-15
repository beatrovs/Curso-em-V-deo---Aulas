#A Confederação Nacional de Natação precisa de um programa 
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
ano = int(input("Escreva o ano do seu nascimento: "))
idade = atual - ano
print("A sua data de nascimento é {} e a sua idade é {}".format(ano, idade))

if idade <= 9:
    print("A sua categoria de competição é MIRIM!")
elif idade <= 14:
    print("A sua categoria de competição é INFANTIL!")
elif idade <= 19:
    print("A sua categoria de competição é JÚNIOR!")
elif idade <= 25:
    print("A sua categoria de competição é SÊNIOR!")
elif idade > 25:
    print("A sua categoria de competição é MASTER!")
