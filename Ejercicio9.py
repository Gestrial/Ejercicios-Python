"""
Ingresar un mail y comprobar si tiene el carácter @. Sino lo tiene informar el error.
"""

email = input("ingresa un email : ")

x = email.find("@")

if x == -1:
    print("No contiene el caracter deseado")
else:
    print("Contiene el caracter deseado")

