#Escribe un programa que pida primero un número par y luego un número impar 
#(positivos o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
#impar respectivamente), se mostrará un aviso.

num_par = int(input("Introduce un número par: "))
num_impar = int(input("Introduce un número impar: "))

if (num_par % 2 != 0) and (num_impar % 2 == 0):
    print("Error: ambos números son incorrectos.")
elif num_par % 2 != 0:
    print("Error: el primer número no es par.")
elif num_impar % 2 != 1:
    print("Error: el segundo número no es impar.")
else:
    print("Los números son correctos.")