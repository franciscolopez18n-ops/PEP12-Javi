# Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
# valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
# bque pida muestre un aviso y vuelva a pedir el valor

import math
# --------------------------------------------------------------
# Funciones para calcular
# --------------------------------------------------------------
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_area_triangulo(base, altura):
    return (base * altura) / 2
def calcular_area_rectangulo(base, altura):
    return base * altura
# --------------------------------------------------------------
# Funciones para las opciones del menú
# --------------------------------------------------------------
def opcion1():
    valido = False

    while not valido:
        radio = float(input("Introduce el radio del círculo: "))
        if radio <= 0:
            print("El radio debe ser mayor que 0")
        else:
            print(f"\nEl área del círculo es: {calcular_area_circulo(radio)}")
            valido = True


def opcion2():
    valido = False

    while not valido:
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))
        if base <= 0 or altura <= 0:
            print("La base y la altura deben ser mayores que 0")
        else:
            print(f"\nEl área del triángulo es: {calcular_area_triangulo(base, altura):.2f}")
            valido = True

def opcion3():
    valido = False

    while not valido:

        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        if base <= 0 or altura <= 0:
            print("La base y la altura deben ser mayores que 0")
        else:
            print(f"\nEl área del rectángulo es: {calcular_area_rectangulo(base, altura):.2f}")
            valido = True
# --------------------------------------------------------------
# Función para mostrar el menú
# --------------------------------------------------------------
def mostrar_menu():
    print("\n--- MENÚ DE CÁLCULO DE ÁREAS ---")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")
# --------------------------------------------------------------
# Función principal
# --------------------------------------------------------------
def main():
    while True:
        mostrar_menu()
        opcion = input("Introduce una opción (1-4): ")
        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida. Introduce un número entre 1 y 4")
# --------------------------------------------------------------
# Inicio del programa 
# --------------------------------------------------------------
if __name__ == "__main__":
    main()
