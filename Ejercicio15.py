"""
Crear un módulo que solicite al usuario el ingreso de un nombre de usuario y
contraseña
criterios de aceptación:
 El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de
12.
 La contraseña debe contener un mínimo de 8 caracteres.
 La contraseña no puede contener espacios en blanco
"""

arrayUsuario = []
arrayContraseña = []
espacioEnblanco = " "

def ejercicio():
    usuario = input("ingresa tu nombre de usuario")
    if len(usuario) < 6 and 12 < len(usuario):
        print("El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12")
        return

    arrayUsuario.append(usuario)
    print("El usuario se guardo correctamente")

    contraseña = input("ingresa tu contraseña")

    if len(contraseña) < 8 and espacioEnblanco in contraseña:
        print("La contraseña debe contener un mínimo de 8 caracteres.La contraseña no puede contener espacios en blanco")
        return

    arrayContraseña.append(contraseña)
    print("La contraseña se guardo correctamente")

ejercicio()


