def a_binario(n):
    return bin(n)[2:]  # indicamos que empieza en el segundo indice para quitar el 0b

def a_hexadecimal(n):
    return hex(n)[2:]  # indicamos que empieza en el segundo indice para quitar el 0b

def a_entero(texto):
    if texto.isdigit():   # control simple de error
        return int(texto)
    else:
        return "Error: el texto no es un número válido"
        