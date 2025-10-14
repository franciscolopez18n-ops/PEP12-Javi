import sys
# --------------------------------------------------------------
# Imports de módulos propios
# --------------------------------------------------------------
from matematicas import operaciones, figuras, conversiones

# --------------------------------------------------------------
# Definición de funciones principales
# --------------------------------------------------------------
def main():
    """Función principal del programa"""
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Operaciones matemáticas")
        print("2. Cálculo de áreas geométricas")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print("Suma:", operaciones.suma(a, b))
            print("Resta:", operaciones.resta(a, b))
            print("Multiplicación:", operaciones.multiplicacion(a, b))
            print("División:", operaciones.division(a, b))

        elif opcion == "2":
            print("\n--- CÁLCULO DE ÁREAS ---")
            print("1. Rectángulo")
            print("2. Triángulo")
            print("3. Círculo")
            tipo = input("Elige una figura (1-3): ")

            if tipo == "1":
                base = float(input("Introduce la base: "))
                altura = float(input("Introduce la altura: "))
                print("Área del rectángulo:", figuras.area_rectangulo(base, altura))

            elif tipo == "2":
                base = float(input("Introduce la base: "))
                altura = float(input("Introduce la altura: "))
                print("Área del triángulo:", figuras.area_triangulo(base, altura))

            elif tipo == "3":
                radio = float(input("Introduce el radio: "))
                print("Área del círculo:", figuras.area_circulo(radio))
            else:
                print("Opción de figura inválida")

        elif opcion == "3":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida. Introduce un número entre 1 y 3")

# --------------------------------------------------------------
# Bloque para asegurar ejecución solo si el archivo es el principal
# --------------------------------------------------------------
if __name__ == "__main__":
    main()