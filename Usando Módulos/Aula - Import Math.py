#Utilizando import math no caso a função de raiz quadrada e arrendodamento.

import math #Para utilizar a biblioteca math necessário fazer o import, não funciona.
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz quadrada do número {} é {}".format(num, math.ceil(raiz)))

...


#Pode ser utilizado também da seguinte forma:

from math import sqrt, floor #Foca apenas em uma função.
num = int(input("Digite um número: "))
raiz = sqrt(num) #Não precisa colocar math.sqrt
print("A raiz quadrada do número {} é {}".format(num, floor(raiz)))


...

#Utilizando import random (gerando um número aleatorio float pelo próprio computador).
import random
num = random.random()
print(num)

...

#Utilizando randit (gerando um número aleatório int pelo próprio computador).
import random
num = random.randint(1, 10)
print(num)

