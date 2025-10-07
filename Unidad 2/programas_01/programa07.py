#Escriba un programa que pida un año y que escriba si es bisiesto o no. Un año es bisiesto
#si es múltiplos de 4 pero no múltiplos de 100, aunque si los múltiplos de 400

año = int(input("Introduce un año: "))

if ((año % 4 == 0) and (año % 100 != 0)) or (año % 400 == 0):
    print("El año ", año, " es bisiesto")
else:
    print("El año ", año, " no es bisiesto")