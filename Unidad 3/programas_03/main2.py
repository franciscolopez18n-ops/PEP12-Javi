import operaciones

# --------------------------------------------------------------
# Definición de funciones principales
# --------------------------------------------------------------
def main():
    """Función principal del programa"""
    print("Hola, este es el programa principal")

    # Pedimos dos números al usuario
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    # Imprimimos las funciones
    print("Suma:", operaciones.suma(a, b))
    print("Resta:", operaciones.resta(a, b))
    print("Multiplicación:", operaciones.multiplicacion(a, b))
    print("División:", operaciones.division(a, b))

if __name__ == "__main__":
    main()