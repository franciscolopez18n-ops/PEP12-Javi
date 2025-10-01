# Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. 
    # El que saque mayor puntuación total, gana. 
    # Si la puntuación total coincide, gana quien haya sacado el dado con el valor más alto.
    # Si el valor más alto también coincide, empatan.

# Puedes pedir el valor de cada tirada de dados por teclado o usar la la función random.randrange(1, 7) 
# para obtener un número aleatorio entre 1 y 6 para ello debes poner import random al inicio del programa
#------------------------------------------------------------------------------------------------------------

import random
#-----------------------------------
# Tiradas jugador 1
dado1_j1 = random.randrange(1, 7)
dado2_j1 = random.randrange(1, 7)
total_j1 = dado1_j1 + dado2_j1
# Dado con mas valor del jugador 1
if (dado1_j1 > dado2_j1):
    mas_alto_j1 = dado1_j1
else:
    mas_alto_j1 = dado2_j1
#-----------------------------------
# Tiradas jugador 2
dado1_j2 = random.randrange(1, 7)
dado2_j2 = random.randrange(1, 7)
total_j2 = dado1_j2 + dado2_j2
# Dado con mas valor del jugador 2
if (dado1_j2 > dado2_j2):
    mas_alto_j2 = dado1_j2
else:
    mas_alto_j2 = dado2_j2
#-----------------------------------
# Mostrar resultados
print("Jugador 1:", dado1_j1, "+", dado2_j1, "=", total_j1)
print("Jugador 2:", dado1_j2, "+", dado2_j2, "=", total_j2)

# Resultado
if (total_j1 > total_j2):
    print("Gana el jugador 1")
elif (total_j2 > total_j1):
    print("Gana el jugador 2")
elif (mas_alto_j1 != mas_alto_j2):
    if (mas_alto_j1 > mas_alto_j2):
        print("Gana el jugador 1 porque ha sacado el dado con el valor más alto")
    else: 
        print("Gana el jugador 2 porque ha sacado el dado con el valor más alto")
else: 
    print("Empate, han sacado los mismos dados")
