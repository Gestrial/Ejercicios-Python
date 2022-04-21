"""
Ejercicio6
En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
realizar un programa que lea los sueldos que cobra cada empleado e informe
cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
Además el programa deberá informar el importe que gasta la empresa en sueldos
al personal.
"""

cantEmpleados = int(input("ingresa la cantidad de empleados"))
sueldoMenor = 0
sueldoMayor = 0

for i in range(cantEmpleados):
        sueldo = int(input("ingresa tu sueldo"))
        if sueldo >=100 and sueldo <300:
            sueldoMenor += 1
        elif sueldo >= 300:
            sueldoMayor += 1

mayor = str(sueldoMayor)
menor = str(sueldoMenor)


print("Los sueldos entre 100 y 300 son = " +menor)
print("Los sueldos mayores a 300 son = " +mayor)

