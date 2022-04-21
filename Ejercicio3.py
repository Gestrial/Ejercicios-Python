"""
Ejercicio3
- Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente
información: cantidad total de preguntas que se le realizaron y la cantidad de
preguntas que contestó correctamente. Se pide confeccionar un programa que
ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje
de respuestas correctas que ha obtenido, y sabiendo que: Nivel máximo:
Porcentaje>=90%.
Nivel medio: Porcentaje>=75% y <90%.
Nivel regular: Porcentaje>=50% y <75%.
Fuera de nivel: Porcentaje<50%.
TAMBIEN PREGUNTARLE AL PELADO
"""

cantPreguntas = int(input("ingrese la cantidad de preguntas"))
preguntasCorrectas = int(input("cantidad de preguntas acertadas"))

porcentajeCorrectas = cantPreguntas * preguntasCorrectas  / 100

if porcentajeCorrectas >= 95:
	print('Nivel Maximo')
if porcentajeCorrectas >= 75 and porcentajeCorrectas <90:
	print('Nivel Medio')
if porcentajeCorrectas >= 50 and porcentajeCorrectas <75:
	print('Nivel Regular')
if porcentajeCorrectas <50:
	print('Fuera de Nivel')


