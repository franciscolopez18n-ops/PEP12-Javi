# Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
# en Python (globales, no locales y locales)

total_puntos = 0

def sumar_puntos_local(puntos):
    # Variable local (solo sirve dentro de esta función)
    puntos_local = puntos + 5

    print("Puntos locales sumados (solo aquí):", puntos_local)

def sumar_puntos_global(puntos):
    # Modifica la variable global
    global total_puntos
    total_puntos += puntos
    print("Total de puntos global actualizado:", total_puntos)

def sumar_puntos_nonlocal():
    # Esto pasa cuando tenemos una función dentro de otra función, creamos una variable
    puntos = 10
    # En esta funcion vamos a modificar la variable que habiamos creado
    def agregar():
        # Variable no local: permite modificar las variables de la función que contiene a otra funcion
        nonlocal puntos
        puntos += 5
        print("Puntos modificados (en la funcion interna):", puntos)
        
    agregar()
    print("Puntos de la funcion externa:", puntos)

# --------------------------------------------------------------
# Programa principal
# --------------------------------------------------------------
print("Pruebas de suma de puntos con diferentes ámbitos")
print("----------------------------------------------------------------")
sumar_puntos_local(3)   # Solo afecta a la variable local
print("Valor final de la variable global total_puntos:", total_puntos)
print("----------------------------------------------------------------")

sumar_puntos_global(3)  # Aumenta la variable global
print("Valor final de la variable global total_puntos:", total_puntos)
print("----------------------------------------------------------------")
sumar_puntos_nonlocal() # Modifica la variable no local dentro de función interna
print("Valor final de la variable global total_puntos:", total_puntos)
