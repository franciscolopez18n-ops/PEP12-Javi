# Escribe un programa para jugar a adivinar un número.
# En primer lugar la aplicación solicita genera un número aleatorio entre 1 y 20.
# A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido.
# El programa termina cuando se acierta el número.
# Puedes generar el número usando la función random.randrange(1, 21) para obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
# del programa).
# Mejora el programa de forma que el usuario tenga solo 3 intentos.

import random

numero_secreto = random.randrange(1, 21)
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    adivina = int(input("Adivina el número entre 1 y 20: "))
    intentos += 1

    if adivina == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        break
    elif adivina < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")

if intentos == max_intentos and adivina != numero_secreto:
    print("Perdiste, el numero secreto es ", numero_secreto)
