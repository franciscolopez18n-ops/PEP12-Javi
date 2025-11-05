import random

vidas_jugador = 3
puntos_j = 0  # para controlar la bonificacion cada 3 puntos
total_puntos = 0
nivel = 1
contador = 0

while vidas_jugador > 0:
    valido = False
    print("El jugador tiene ", vidas_jugador, " vidas")
    print("Puntos: ", total_puntos, "\n")
    print("Ataques:")
    print("1. fuerza")
    print("2. precision")
    print("3. riesgo")

    try:
        opcion = int(input("Seleccione una de las opciones: "))
        print("-----------------------------")
        match opcion:
            case 1:
                carta_jugador = random.randint(5, 10)
                carta_cpu = random.randint(3, 10)
                valido = True

            case 2:
                carta_jugador = random.randint(3, 8)
                carta_cpu = random.randint(2, 9)
                valido = True
            case 3:
                carta_jugador = random.randint(1, 10)
                carta_cpu = random.randint(1, 8)
                valido = True
            case _:

                print("Carta invalida")
                print("-----------------------------")

        if valido:
            print("Jugador: ", carta_jugador)
            print("CPU: ", carta_cpu)

            if carta_jugador > carta_cpu:
                print("-----------------------------")
                print("Ganaste el turno")
                print("-----------------------------")
                puntos_j += 1
                total_puntos += 1
            elif carta_jugador == carta_cpu:
                print("-----------------------------")
                print("Empate")
                print("-----------------------------")
            else:
                print("-----------------------------")
                print("Perdiste el turno")
                print("-----------------------------")
                vidas_jugador -= 1

            if puntos_j == 3 and contador < 3:
                contador += 1  # numero de veces que recupera vidas
                puntos_j = 0  # reiniciamos
                vidas_jugador += 1
                nivel += 1
                print("El jugador recupero 1 vida \n")

    except ValueError:
        print("-----------------------------")
        print("Debes introducir una opcion valida")
        print("-----------------------------")

print("FIN DE LA PARTIDA: ")
print("Puntuacion: ", total_puntos)
print("Nivel alcanzado: ", nivel)
