import random
import time
import sys

print("Hola, soy Roberto")
print("Vamos jugar un juego, voy intentar averiguar el numero en el que estas pensando con el menor intentos posibles")


time.sleep(3)

min=0
max=100
guess = 50
x=0

print("El numero debe estar entre "+str(min)+" y "+str(max))

while not x==3:

    print("Es..."+str(guess)+" tu numero?")
    print("==================================================================================")
    print("1 -Es más alto, ")
    print("2 -Es más bajo")
    print("3 - Acertaste! Eres increible, el mejor de todos!")
    x = int(input())
    
    if (x==1):
        min=guess
        
    elif (x==2):
        max=guess

    elif (x!=3):
        print("Por favor, abstente de golpear el teclado con la cabeza para pulsar los numeros")

    guess=random.randint(min, max)
