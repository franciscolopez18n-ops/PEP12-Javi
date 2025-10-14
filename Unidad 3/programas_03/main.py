# Importamos el modulo
import operaciones

def main():

    # Pedimos dos números al usuario
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    # Mostramos resultados usando el módulo operaciones
    print("Suma:", operaciones.suma(a, b))
    print("Resta:", operaciones.resta(a, b))
    print("Multiplicación:", operaciones.multiplicacion(a, b))
    print("División:", operaciones.division(a, b))

if __name__ == "__main__":
    main()