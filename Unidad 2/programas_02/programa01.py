# Escribe un programa que muestre una lista de números del 1 al 10.
# Resuelve el ejercicio de dos formas distintas, utilizando los bucles for y while.
# Cuando utilices el bucle for puedes hacer uso de la función range

# ----------------------- TEORIA -------------------------------------#
# range(inicio, fin, paso)
# inicio: valor inicial (inclusive, se incluye en la secuencia)
# fin: valor final (exclusive, no se incluye en la secuencia)
# paso: cuánto se incrementa o decrementa en cada iteración (opcional, por defecto 1)
# -----------------------------------------------------------------------#

# Bucle for
print("Usando bucle for:")

for i in range(1, 11):
    print(i)

# Bucle while
print("\nUsando bucle while:")
i = 1

while i <= 10:
    print(i)
    i += 1
