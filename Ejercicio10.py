"""
Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se
ingresaron. Tener en cuenta que un espacio en blanco es igual a " ", en cambio una
cadena vacía es ""
"""

oracion = input("ingresa una oracion")
acc = 0

for i in oracion:
    if i == " ":
        acc += 1

print(acc)