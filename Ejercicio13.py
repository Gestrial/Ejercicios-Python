"""
Solicitar la carga del nombre de n personas en mayúscula. Mostrar un mensaje si
comienza con vocal dicho nombre.

"""

vocales = ["A","E","I","O","U"]

cantPersonas = input("cantidad de personas")

for i in cantPersonas:
    nombre = input("ingresa tu nombre")
    for j in vocales:
        if nombre[i]-1 == vocales[j]-1:
            
