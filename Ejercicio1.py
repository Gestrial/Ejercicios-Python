"""
ejercicio 1
Desarrollar un programa que permita la carga de 12 valores por teclado y nos
muestre posteriormente la suma de los valores ingresados y su promedio. El
resultado del promedio es un valor real es decir con coma. Si queremos que el
resultado de la división solo retorne la parte entera del promedio debemos utilizar el
operador //: promedio=suma//12

"""
acc = 0

for i in range(12):
    valor = int(input("ingrese un valor"))
    acc += valor

promedio = acc / 12

print(promedio)