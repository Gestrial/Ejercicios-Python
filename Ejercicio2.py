"""
Ejercicio2
Desarrollar un programa que nos permita ingresar 10 número y nos diga si cada
número es par o impar. Para lo cual utilizar el operador % que nos devuelve el
resto de la División

"""

for i in range(10):
    valor = int(input("ingrese un valor"))
    if valor % 2 == 0:
        print('El número', valor, 'es par.')
    else:
        print('El número', valor, 'es impar.')
