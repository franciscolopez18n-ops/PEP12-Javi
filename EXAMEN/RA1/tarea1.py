minutos = int(input("Introduce una cantidad de minutos: "))

horas = minutos // 60  # hora sin decimales
resto = minutos - horas * 60

print("Equivale a ", horas, " horas y ", resto, " minutos")  # se concatena con ","
