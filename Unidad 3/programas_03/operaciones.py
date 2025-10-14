#Crea un módulo llamado operaciones que contenga cuatro funciones básicas relacionadas con operaciones numéricas:
#    suma(a, b) → devuelve la suma de dos números.
#    resta(a, b) → devuelve la resta de dos números.
#    multiplicacion(a, b) → devuelve la multiplicación de dos números.
#    division(a, b) → devuelve la división de dos números (controlando la división entre cero)
# Crea un programa principal main.py que y importe el módulo matemáticas, pida al usuario
# dos números y muestre los resultados de aplicar cada una de las funciones anteriores.
# operaciones.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división entre cero"
    return a / b
