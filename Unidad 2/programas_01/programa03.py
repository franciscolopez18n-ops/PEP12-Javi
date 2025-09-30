#Escribe un programa que pida dos numero y muestre su división. Se deben tener en
#cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num2 == 0:
    print("Error: no se puede dividir por 0.")
else:
    print("Resultado:", num1/num2)