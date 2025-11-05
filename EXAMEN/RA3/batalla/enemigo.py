import random


def generar_enemigo():
    nombres = ["Hydra", "Kraken", "Minotauro", "Gorgona", "Titan"]

    nombre = random.choice(nombres)
    conocimiento = random.randint(1, 10)
    energia = random.randint(1, 5)

    datos = [nombre, conocimiento, energia]

    return datos


def ataque_enemigo(conocimiento, energia):
    nivel_magia = (conocimiento * energia) * random.randint(1, 3)
    return nivel_magia


def mostrar_enemigo(nombre, conocimiento, energia):
    print("----------------------------")
    print("Enemigo: ", nombre)
    print("   Conocimiento: ", conocimiento)
    print("   Energia: ", energia, "\n")
