"""
Ejercicio6
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
realizar un programa que lea los sueldos que cobra cada empleado e informe
cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
Además el programa deberá informar el importe que gasta la empresa en sueldos
al personal.
Me falta la logica de probar con muchos empleados a la ves.
"""

sueldoMenor = 0
sueldoMayor = 0
gastoSueldos = 0

sueldo = int(input("ingresa tu sueldo"))
if sueldo < 300:
    sueldoMenor += 1
else:
    sueldoMayor += 1
gastoSueldos += sueldo


print("Los sueldos entre 100 y 300 son = " +str(sueldoMenor))
print("Los sueldos mayores a 300 son = " +str(sueldoMayor))
print("El importe que gasta la empresa en sueldos en personal es :" +str(gastoSueldos))

