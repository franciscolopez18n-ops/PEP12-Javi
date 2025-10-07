# Escribe un programa para jugar a una versión muy simplificada del black jack.
# En primer lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada).
# A continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando para obtener su puntuación,
# hasta que el quiera.
# Si se pasa de 21 pierde,
# si obtiene una puntuación igual o menor que la banca pierde
# y si obtiene una puntuación superior a la banca gana.

import random

banca = random.randint(17, 21)
print("La banca tiene un número secreto entre 17 y 21")

puntos = 0

while True:
    carta = random.randint(1, 5)
    puntos += carta
    print(f"Has sacado {carta}, total de puntos: {puntos}")

    # Si te pasas pierdes
    if puntos > 21:
        print("¡Te has pasado de 21! Pierdes.")
        break

    print("----------------------------------------")
    # Preguntar si quiere otra carta
    opcion = int(
        input("¿Quieres otra carta? \n Si(1) \n No(2) \n Selecciona una opcion: ")
    )
    while opcion < 1 or opcion > 2:
        opcion = int(input("Introduce una opcion valida: "))
    print("----------------------------------------")
    if opcion == 2:
        # Comprueba
        if puntos > banca:
            print(f"¡Ganaste! Banca: {banca}, Tus puntos: {puntos}")
        else:
            print(f"Perdiste. Banca: {banca}, Tus puntos: {puntos}")
        salida = 2
        break
