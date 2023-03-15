nome = str(input("Qual o seu nome? "))

if nome == "Beatriz":
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria":
    print("O seu nome é bem comum no Brasil!")
else:
    print("O seu nome é bem normal!")
print("Tenha um ótimo dia, {}!".format(nome))
