"""
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de
caracteres. Controlar que el string ingresado tenga entre 10 y 20 caracteres para
que sea válido, en caso contrario mostrar un mensaje de error.
"""

array = []

clave = input("ingresa una clave")
if len(clave) <10 or len(clave) >20:
    print("ingresa una clave correcta")
else:
    array.append(clave)
    print("La clave se guardo exitosamente")
    print(array)


