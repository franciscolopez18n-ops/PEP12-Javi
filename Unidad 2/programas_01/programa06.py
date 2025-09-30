#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

if (mes < 1) or (mes > 12):
    print("Mes incorrecto")
else:
    #meses con 31 dias
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if (1 <= dia) and (dia <= 31):
            print("Fecha correcta")
        else:
            print("Día incorrecto")
    #meses con 30 dias
    elif mes in [4, 6, 9, 11]:
        if (1 <= dia) and (dia <= 30):
            print("Fecha correcta")
        else:
            print("Día incorrecto")
    elif mes == 2:
        # Comprobamos si es año bisiesto
        if ((año % 4 == 0 )and (año % 100 != 0)) or (año % 400 == 0):
            if (1 <= dia) and (dia <= 29):
                print("Fecha correcta")
            else:
                print("Día incorrecto")
        else:
            if (1 <= dia) and (dia<= 28):
                print("Fecha correcta")
            else:
                print("Día incorrecto")