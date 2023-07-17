# Capturar lista de números del usuario
entrada = input("Ingresa una lista de números separados por comas: ")
lista_numeros = [int(num) for num in entrada.split(",")]
#Capturar valor X
valorx = int(input("Ingresa el numero objetivo X: "))


def findIndices(numList, aim):
    numberDictionary = {}  # Diccionario para almacenar los números y sus índices
    # Recorrer la lista de enteros y buscar los pares cuya suma sea igual a x
    for i, num in enumerate(numList):
        complement = aim - num #Obtenemos el complemento
        if complement in numberDictionary: # Si complemento existe en el diccionario de numeros
            return [numberDictionary[complement], i] #regresa el indice actual y el indice que se encuentra en el diccionario de numeros con la key del complemento 
        numberDictionary[num] = i #se asigna el indice al diccionario de numeros con la key del numero del array
    return None

print(findIndices(lista_numeros,valorx))