"""
Ejercicio8
- Una planta que fabrica perfiles de hierro posee un lote de n piezas.
Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a
procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya 
SSentis que la consiga entra incompleta....
"""

cantPiezas = int(input("ingresa la cantidad de piezas"))
piezasEnregla = 0
for i in range(cantPiezas):
    longitudPieza = float(input("ingrese la longitud de la pieza"))
    if longitudPieza >= 1.20 and longitudPieza <= 1.30:
        piezasEnregla += 1

totalPiezas = str(piezasEnregla)

print("La cantidad de piezas en reglas son =" +totalPiezas)