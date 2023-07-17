# Capturar lista de strings del usuario
lista_strings = input("Ingresa una lista de strings separados por comas: ").split(",")

def obtener_anagramas(lista):
    anagramas = []
    no_anagramas = []
    for i in range(len(lista)):
        grupo = [lista[i]]
        anagrama_encontrado = False
        for j in range(i + 1, len(lista)):
            if sorted(lista[i]) == sorted(lista[j]):
                grupo.append(lista[j])
                anagrama_encontrado = True
        if anagrama_encontrado:
            anagramas.append(tuple(grupo))
        else:
            no_anagramas.append(lista[i])
    return anagramas + [("No anagramas:",) + tuple(no_anagramas)]

# Eliminar espacios en blanco alrededor de cada string
lista_strings = [s.strip() for s in lista_strings]

# Obtener lista de anagramas
anagramas = obtener_anagramas(lista_strings)

# Imprimir resultados
print("Anagramas encontrados:")
for grupo in anagramas:
    print(grupo)