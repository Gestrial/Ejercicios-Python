"""
Ejercicio7
Se necesita realizar un control de edad de ingreso al Sistema de una empresa.
Mientras la edad sea entre 18 y 65 pueden acceder al sistema caso contrario
mostrar Mensaje de Acceso Denegado

"""
edad = int(input("ingrese su edad"))
if edad < 18:
    print("Acceso Denegado")
elif edad > 65:
    print("Acceso Denegado")
else:
    print("Bienvenido")