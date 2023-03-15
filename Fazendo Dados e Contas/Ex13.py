#Escreva um programa que converta uma temperatura digitando 
# em graus Celsius e converta para graus Fahrenheit.

TC = float(input("Qual a temperatura na sua cidade °C ? "))
TF = ((9 * TC)/ 5) + 32
tempF= print("A temperatura em C era de {} °C, para Fahrenheit é de {} °F ".format(TC, TF))