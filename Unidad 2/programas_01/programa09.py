# Escribe un programa en Python que simule el juego de piedra, papel o tijera.
# En primer lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle qué opción desea elegir.
# Por ejemplo:
# 1. Piedra
# 2. Papel
# 3. Tijera
# Seleccione una opción (1, 2 o 3):

# Después de leer la opción seleccionada por el usuario el programa generará un número aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
# ganado o ha perdido dependiendo del resultado.

# Ten en cuenta que:
# • La piedra gana a la tijera pero pierde contra el papel.
# • El papel gana a la piedra pero pierde contra la tijera.
# • La tijera gana al papel pero pierde contra la piedra.

import random

print("Bienvenido al juego de piedra, papel o tijera.")
print("Opciones:")
print("\t 1. Piedra", "\n\t 2. Papel", "\n\t 3. Tijera")
opcion_player = int(input("Seleccione una opción (1, 2 o 3): "))

opcion_cpu = random.randrange(1, 3)


# ------------------------------------------------------------------------------
# FUNCION PARA INDICAR LA JUGADA (se tiene que colocar ANTES de )
def jugada(opcion):
    match opcion:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"
        case _:
            return "Opción no válida"


# ------------------------------------------------------------------------------
print("----------------------")
print("Jugada del jugador: ", jugada(opcion_player))
print("Jugada de la CPU: ", jugada(opcion_cpu))
# ------------------------------------------------------------------------------
print("----------------------")
if opcion_player == opcion_cpu:
    print("Empate")
elif opcion_player == 1 and opcion_cpu == 2:
    print("Gana la CPU")
elif opcion_player == 1 and opcion_cpu == 3:
    print("Gana el Jugador")

elif opcion_player == 2 and opcion_cpu == 1:
    print("Gana el Jugador")
elif opcion_player == 2 and opcion_cpu == 3:
    print("Gana la CPU")

elif opcion_player == 3 and opcion_cpu == 1:
    print("Gana la CPU")
elif opcion_player == 3 and opcion_cpu == 2:
    print("Gana el Jugador")
