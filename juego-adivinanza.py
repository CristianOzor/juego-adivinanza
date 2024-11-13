import random
from os import system

numero_secreto = random.randint(0,101)
adivinado = False
cant_intentos = 0
cant_max_intentos = 5

system("cls")
print("¡Bienvenido al juego de adivinar el número secreto!")

while not adivinado:

    if not cant_intentos < cant_max_intentos:
        print("\n¡Game Over! No has podido adivinar dentro de los 5 intentos\n")
        break


    numero = int(input("Introduce un número del 1 al 100:\n "))

    if numero == numero_secreto:
        system("cls")
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    
    elif numero < numero_secreto:
        system("cls")
        print("El número es mayor al ingresado")
    
    else:
        system("cls")
        print("El número es menor al ingresado")

    cant_intentos += 1



#Otra manera de hacerlo
"""while not adivinado and cant_intentos < cant_max_intentos:
    numero = int(input("Introduce un número del 1 al 100:\n "))

    if numero == numero_secreto:
        system("cls")
        print("¡Felicitaciones has adivinado el número secreto!")
        adivinado = True
    
    elif numero < numero_secreto:
        system("cls")
        print("El número es mayor al ingresado")
    
    else:
        system("cls")
        print("El número es menor al ingresado")

    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print("\n¡Game Over! No has podido adivinar dentro de los 5 intentos\n")"""

