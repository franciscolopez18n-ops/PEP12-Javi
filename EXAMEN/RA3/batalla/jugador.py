import random


def ataque_jugador(conocimiento, energia):
    nivel_magia = (conocimiento * energia) * random.randint(1, 3)
    return nivel_magia


def mostrar_jugador(nombre, conocimiento, energia):
    print("Jugador/a: ", nombre)
    print("   Nivel de conocimiento: ", conocimiento)
    print("   Energia: ", energia, "\n")
