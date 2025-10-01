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
print("\t 1. Piedra","\n\t 2. Papel", "\n\t 3. Tijera")
opcion_player = int(input("Seleccione una opción (1, 2 o 3): "))

if opcion_player<1 or opcion_player

opcion_cpu = random.randrange(1, 3)

if opcion_player == opcion_cpu:
    print("Empate")
elif opcion_player==1 and opcion_cpu == 2:
    print("Empate")




