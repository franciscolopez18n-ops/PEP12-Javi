# Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
# suma y la media de todos los números introducidos.
# Realiza dos versiones: una que utiliza la instrucción break y otra no

# Version con Break (como condicion ponemos True para que se ejecute)
suma = 0
contador = 0
print("----------------------------------------")
print("Version con Break \nIntroduce numeros hasta introducir un 0\n")
while True:
    numero = int(input("Numero: "))
    if numero == 0:
        break

    suma += numero
    contador += 1
    media = suma / contador

    print("    Suma: ", suma, "\n    Media: ", media)

print("----------------------------------------")

# Version sin Break
print("Version sin Break: \nIntroduce numeros hasta introducir un 0\n ")
numero = -1
suma = 0
contador = 0

while numero != 0:
    numero = int(input("Numero: "))

    suma += numero
    contador += 1
    media = suma / contador

    print("    Suma: ", suma, "\n    Media: ", media)
