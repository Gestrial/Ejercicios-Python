"""
Ejercicio4
Escribir un programa que solicite ingresar n notas de alumnos y nos informe
cuántos tienen notas mayores o iguales a 7 y cuántos menores. Cuando ingresa
nota=0 termina la ejecución
"""

ccmayor = 0
ccmenor = 0

nota = -1

while nota != 0:
    nota = int(input("ingrese su nota :"))
    if nota == 0:
        break

    if nota >= 7:
        ccmayor += 1
    else:
        ccmenor += 1

print("Notas Mayores o iguales a 7:" + str(ccmayor))
print("Notas menores:" + str(ccmenor))
