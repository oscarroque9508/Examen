# Capturar cadena de texto del usuario
texto = input("Ingresa una cadena de texto: ")

def invertir_string(string):
    if len(string) == 0:
        return ""
    else:
        return invertir_string(string[1:]) + string[0]

# Obtener el inverso de la cadena
inverso = invertir_string(texto)

# Imprimir resultados
print("Cadena original:", texto)
print("Inverso:", inverso)