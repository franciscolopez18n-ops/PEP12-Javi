#Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
#qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
#de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
#similar al siguiente:
#     1. Calcular el área de un círculo
#     2. Calcular el área de un triángulo
#     3. Calcular el área de un rectángulo
#     4. Salir
#     Introduce una opción (1-4):
# El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la opción 4.

# Hay que diseñar y definir la siguientes funciones: :
#     • calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y
#       retorna su área.
#     • calcular_area_triangulo: recibe como parámetros de entrada la base y la altura
#       del triangulo y retorna su área.
#     • calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura
#       del rectángulo y retorna su área.
#     • mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.
#     • main(): lee por teclado la opción seleccionada por el usuario, valida que la opción
#       está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función
#       correspondiente en función de la opción seleccionada.
#     • opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre
#       sea mayor que 0 y una vez que ha validado el radio llamará a la función
#       calcular_area_circulo.
#     • opcion2: descripción: lee por teclado el valor de la base y la altura del triángulo,
#       valida que los dos datos son mayores que 0 y una vez que los ha validado llamará
#       a la función calcular_area_triangulo.
#     • opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que
#       los dos datos son mayores que 0 y una vez que los ha validado llamará a la función
#       calcular_area_rectangulo


# EL ORDEN DE LAS FUNCIONES IMPORTA

import math  # Para usar el número pi

# --------------------------------------------------------------
# Funciones para calcular
# --------------------------------------------------------------

def calcular_area_circulo(radio):
    """Calcula el área de un círculo a partir de su radio"""
    return math.pi * radio ** 2

def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo a partir de su base y altura"""
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo a partir de su base y altura"""
    return base * altura

# --------------------------------------------------------------
# Funciones para las opciones del menú
# --------------------------------------------------------------

def opcion1():
    """Lee el radio del círculo, comprueba que sea > 0 y muestra el área"""
    radio = float(input("Introduce el radio del círculo: "))
    if radio <= 0:
        print("El radio debe ser mayor que 0")
    else:
        area = calcular_area_circulo(radio)
        print(f"\nEl área del círculo es: {area}")

def opcion2():
    """Lee la base y la altura del triángulo y muestra el área."""
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    area = calcular_area_triangulo(base, altura)
    print(f"\nEl área del triángulo es: {area}")

def opcion3():
    """Lee la base y la altura del rectángulomuestra el área."""
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))
    area = calcular_area_rectangulo(base, altura)
    print(f"\nEl área del rectángulo es: {area}")

# --------------------------------------------------------------
# Función para mostrar el menú
# --------------------------------------------------------------

def mostrar_menu():
    """Muestra el menú principal por pantalla."""
    print("\n--- MENÚ DE CÁLCULO DE ÁREAS ---")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

# --------------------------------------------------------------
# Función principal
# --------------------------------------------------------------

def main():
    """Lee la opción del usuario y ejecuta la función correspondiente"""
    valido = False

    while not valido:
        mostrar_menu()
        opcion = input("Introduce una opción (1-4): ")

        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            print(" Saliendo del programa...")
            valido = True
        else:
            print("Opción inválida. Por favor, introduce un número entre 1 y 4.\n")

# --------------------------------------------------------------
# Inicio del programa (indicamos la primera funcion que se va a ejecutar)
# --------------------------------------------------------------


if __name__ == "__main__":
    main()