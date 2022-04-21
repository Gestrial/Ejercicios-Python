"""
Solicitar la carga del nombre de n personas en mayúscula. Mostrar un mensaje si
comienza con vocal dicho nombre.

"""

vocales = ["A","E","I","O","U"]

cantPersonas = int(input("cantidad de personas"))

for i in range(cantPersonas):
    nombre = input("ingresa tu nombre")
    for vocal in vocales:
        if nombre.startswith(vocal):
            print("Dicho nombre comienza con vocal")
