"""
-Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales),
isósceles (dos lados iguales), o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.
"""


cantTriangulos = int(input("Ingresa la cantidad de triangulos"))

equilatero = 0
isósceles = 0
escaleno = 0

for i in range(cantTriangulos):
    lado1 = input("ingresa un primer lado")
    lado2 = input("ingresa un segundo lado")
    lado3 = input("ingresa un tercer lado")
    if lado1 == lado2 and lado2 == lado3:
        equilatero += 1
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        isósceles += 1
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        escaleno += 1



print("La cantidad de triangulos equilatero son =" +str(Equilatero))
print("La cantidad de isósceles equilatero son =" +str(Isosceles))
print("La cantidad de escaleno equilatero son =" +str(Escaleno))
