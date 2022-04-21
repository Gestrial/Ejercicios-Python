"""
Ejercicio5
- Ingresan las alturas n personas y se calcula el promedio. Preguntar cuántos datos
se ingresarán
"""

cantIngresos = int(input("ingresa la cantidad de ingresos"))
cantTotalalturas = 0

for i in range(cantIngresos):
    altura = int(input("ingresa tu altura"))
    cantTotalalturas += altura

promedio = cantTotalalturas / cantIngresos

print(promedio)
