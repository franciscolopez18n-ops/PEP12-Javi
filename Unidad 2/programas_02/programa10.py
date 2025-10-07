# Modifica el programa anterior para que pida en primer lugar el número de jugadores que
# van a jugar.
# Cada jugador irá jugando y el programa mostrará si ha ganado o no a la banca.

import random

print("----------------------------------------")

# Pedimos el número de jugadores
num_jugadores = int(input("Introduce el número de jugadores: "))

# La banca saca un numero
banca = random.randint(17, 21)
print("\nLa banca tiene un número secreto entre 17 y 21\n")

resultados = ""

# Bucle para que cada jugador juegue su turno
for i in range(1, num_jugadores + 1):
    print(f"--------------- TURNO DEL JUGADOR {i} ---------------\n")
    puntos = 0

    while True:
        carta = random.randint(1, 5)
        puntos += carta
        print("Has sacado", carta, "total de puntos:", puntos, "\n")

        # Si se pasa de 21 pierde
        if puntos > 21:
            print("Te has pasado de 21. Perdiste\n")
            resultados += "Jugador " + str(i) + ": Perdio\n"  # convertimos a cadena
            break

        # Preguntar si quiere otra carta
        opcion = int(
            input("¿Quieres otra carta? \nSi(1) \nNo(2)\n\nSelecciona una opción: ")
        )
        while opcion < 1 or opcion > 2:
            opcion = int(input("Introduce una opción válida (1 o 2): "))

        print(f"\n------------- RESULTADO DEL JUGADOR {i} -------------\n")
        if opcion == 2:
            if puntos > banca:
                print(f"Banca: {banca} \nTus puntos: {puntos}\nGanaste jugador {i}\n")
                resultados += "Jugador " + str(i) + ": Gano\n"

            else:
                print(f"Banca: {banca} \nTus puntos: {puntos}\nPerdiste jugador {i}\n")
                resultados += "Jugador " + str(i) + ": Perdio\n"

            break

print("------------------ FIN DEL JUEGO ------------------\n")
print(resultados)
