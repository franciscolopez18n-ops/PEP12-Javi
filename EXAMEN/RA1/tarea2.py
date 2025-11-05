# Pide al usuario
entero = int(input("Introduce un número entero: "))
decimal = float(input("Introduce un decimal: "))
cadena = input("Introduce una cadena: ")

# Mostrar valor y el tipo
print("\nEl numero entero es de tipo", type(entero), " y su valor es: ", entero)
print("El numero decimal es de tipo", type(decimal), " y su valor es: ", decimal)
print("La cadena es del tipo", type(cadena), " y su valor es: ", cadena, "\n")

# Comprueba si es del tipo correcto y lo guarda en un booleano
es_entero = isinstance(entero, int)
es_decimal = isinstance(decimal, float)
es_cadena = isinstance(cadena, str)

# Muestra si todas son correctas o no
print("Comprobaciones: \n")
print(entero, " comprobacion: ", es_entero)
print(decimal, " comprobacion: ", es_decimal)
print(cadena, " comprobacion: ", es_cadena)


print("La suma es ", entero + decimal)
