# Escribe un programa que realice las siguientes operaciones:
#    1. Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que no se introduzca el número correcto.
#    2. Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
#    3. Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
#       desea introducir otro número o no. Si el usuario selecciona que quiere continuar el programa tendrá que volver a ejecutarse
#       y repetir los mismos pasos. Si el usuario indica que no quiere continuar el programa finaliza

salida = 1
while salida == 1:
    num = int(input("Introduce un número entre 1 y 10: "))

    # Comprobar si es valido
    while num < 1 or num > 10:
        num = int(input("Numero incorrecto. Introduce un número entre 1 y 10: "))
    print("----------------------------------------")

    # Mostrar tabla de multiplicar
    print(f"Tabla de multiplicar del {num}:")
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
        # Otra forma de escribirlo: print(f"{num} x {i} = {num*i}")
    print("----------------------------------------")

    # Preguntar si quiere continuar(s/n)
    respuesta = int(
        input(
            "¿Quieres introducir otro número? \n Si(1) \n No(2) \n Selecciona una opcion: "
        )
    )
    while respuesta < 1 or respuesta > 2:
        respuesta = int(input("Introduce una opcion valida: "))
    print("----------------------------------------")

    if respuesta == 2:
        print("Programa finalizado")
        salida = 2
    else:
        print("Reiniciando el programa")
    print("----------------------------------------")
