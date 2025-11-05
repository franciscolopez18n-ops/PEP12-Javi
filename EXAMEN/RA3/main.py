import sys

# --------------------------------------------------------------
# Imports de módulos propios
# --------------------------------------------------------------
from batalla import enemigo, jugador


def main():
    print("=== BATALLA DE MAGIA ===\n")
    rondas = 0
    datos_cpu = []

    nombre = input("Introduce tu nombre: ")

    try:
        conocimiento = int(input("Nivel de conocimiento (1-10): "))
        while conocimiento < 1 or conocimiento > 10:
            conocimiento = int(input("Introduce un nivel valido (1-10): "))

        energia = int(input("Energia inicial (1-5): "))
        while energia < 1 or energia > 5:
            energia = int(input("Introduce una energia valida (1-5): "))

        print("-----------------------------")
        datos_cpu = enemigo.generar_enemigo()  # nombre, conocimiento, energia
        jugador.mostrar_jugador(nombre, conocimiento, energia)
        enemigo.mostrar_enemigo(datos_cpu[0], datos_cpu[1], datos_cpu[2])

        while rondas < 3:
            print("=== RONDA ", rondas + 1, " ===")
            magia_jugador = jugador.ataque_jugador(conocimiento, energia)
            magia_cpu = enemigo.ataque_enemigo(datos_cpu[1], datos_cpu[2])
            print("Magia de ", nombre, ": ", magia_jugador)
            print("Magia de ", datos_cpu[0], ": ", magia_cpu)

            if magia_jugador > magia_cpu:
                print(nombre, " lanza un hechizo poderoso! (-1 energia enemigo)\n")
                datos_cpu[2] -= 1

            elif magia_jugador == magia_cpu:
                print("Empate \n")
            else:
                print(
                    datos_cpu[0],
                    " responde con un conjuro devastador! (-1 energia jugador)\n",
                )
                energia -= 1

            rondas += 1

        print("=== FIN DEL DUELO ===")

        if energia > datos_cpu[2]:
            print("¡", nombre, " ha vencido a ", datos_cpu[0], "!")
        elif energia == datos_cpu[2]:
            print("Empate")
        else:
            print("¡", nombre, " perdio contra ", datos_cpu[0], "!")

    except ValueError:
        print("Debes introducir números")


# --------------------------------------------------------------
# Se ejecuta automaticamente
if __name__ == "__main__":
    main()
