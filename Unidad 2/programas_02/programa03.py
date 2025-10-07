# Escribe un programa que muestre los números pares que hay entre 0 y 10.
# Resuelve el ejercicio de 4 formas diferentes.
# Usando los bucles for y while sin y con la sentencia continue

# Clave: imprime cuando SI es par (comprueba si ES par)
print("Bucle for sin continue:")
for i in range(11):
    if i % 2 == 0:
        print(i)

# Clave: NO imprime cuando es impar (comprueba si NO es par)
print("Bucle for con continue:")
for i in range(11):
    # Cuando el resultado NO es igual a 0 NO es par y salta a la siguiente
    if i % 2 != 0:
        continue  # Seria como un Break, cuando se ejecuta lo que se encuentra debajo NO se ejecuta, sino que pasa a la siguiente iteracion

    print(i)

print("----------------------------")

print("Bucle while sin continue:")
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

print("Bucle while con continue:")
i = 0
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1
