"""
Ingresar una oración que pueden tener letras tanto en mayúsculas como
minúsculas. Contar la cantidad de vocales.
"""

vocales = ["A","E","I","O","U"]

oracion = input("Ingresa una oracion \n")

cantVocales = 0

for i in oracion:
    for vocal in vocales:
        if i.lower() == vocal.lower():
            cantVocales += 1

print(cantVocales)

