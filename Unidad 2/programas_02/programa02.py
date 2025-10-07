# Escribe un programa que lea por teclado un número comprendido entre 1 y 10. No se dejara de
# pedir el número hasta que no se introduzca correctamente.

numero = int(input("Introduce un numero dentro del rango [1, 10]: "))
while (numero < 1) or (numero > 10):
    numero = int(
        input("Numero invalido, el numero debe estar dentro del intervalo [1-10]: ")
    )

print("El numero ", numero, " es un numero valido")
