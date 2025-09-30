# Escribe un programa que use varias veces la función print() para
# - Mostrar operaciones de los operadores aritméticos de Python entre dos números.
# - Mostrar operaciones de los operadores lógicos de Python con valores booleanos.
# - Mostrar operaciones de los operadores de comparación de Python con valores booleanos y/o números.

a = 10
b = 5

# Operadores aritméticos
print("Suma:", a, "+", b, "=", a + b)
print("Resta:", a, "-", b, "=", a - b)
print("Multiplicación:", a, "*", b, "=", a * b)
print("División:", a, "/", b, "=", a / b)
print("División entera:", a, "//", b, "=", a // b) #Quita los decimales
print("Módulo:", a, "%", b, "=", a % b)
print("Potencia:", a, "**", b, "=", a ** b)

# Operadores lógicos
x = True
y = False
print("AND:", x, "and", y, "=", x and y)
print("OR:", x, "or", y, "=", x or y)
print("NOT:", "not", x, "=", not x)

# Operadores de comparación
print("== :", a, "==", b, "=", a == b)
print("!= :", a, "!=", b, "=", a != b)
print(">: ", a, ">", b, "=", a > b)
print("<: ", a, "<", b, "=", a < b)
print(">=: ", a, ">=", b, "=", a >= b)
print("<=: ", a, "<=", b, "=", a <= b)