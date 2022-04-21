"""
Ejercicio4
Escribir un programa que solicite ingresar n notas de alumnos y nos informe
cuántos tienen notas mayores o iguales a 7 y cuántos menores. Cuando ingresa
nota=0 termina la ejecución
PREGUNTARLE AL PELADO POR QUE ESTOY QUEMADO
"""
notas = 0
notas2 = 0
cantNotaslumnos = int(input("ingrese la cantidad de notas :"))
notaAlumno = 1
while notaAlumno != 0:  
    for i in range(cantNotaslumnos):
        notaAlumno = int(input("ingrese su nota :"))
        if notaAlumno >= 7:
            notas += 1
        else:
            notas2 += 1

print(notas)
print(notas2)