#Crie um programa que leia o nome de uma cidade 
# e diga se ela começa com ou não com o nome "Santo"

cidade = str(input("Qual a sua cidade? ")).strip()
print(cidade[:5].upper() == "SANTO") #5 pela quantidade de letras que tem em "Santo", lembrando -1
