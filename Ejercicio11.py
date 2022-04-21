"""
Ingresar una oración que pueden tener letras tanto en mayúsculas como
minúsculas. Contar la cantidad de vocales.
PREGUNTARLE AL PELADO
"""

vocales = ["A","E","I","O","U"]

oracion = input("Ingresa una oracion")

cantVocales = 0

for i in range(oracion):
    for vocal in vocales:
        if i == vocal or i == vocal.lower:
            cantVocales += 1

print(cantVocales)

