"""
Ejercicio3
- Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente
información: cantidad total de preguntas que se le realizaron y la cantidad de
preguntas que contestó correctamente. Se pide confeccionar un programa que
ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje
de respuestas correctas que ha obtenido, y sabiendo que: 
Nivel máximo: Porcentaje>=90%.
Nivel medio: Porcentaje>=75% y <90%.
Nivel regular: Porcentaje>=50% y <75%.
Fuera de nivel: Porcentaje<50%.
"""

cantPreguntas = int(input("ingrese la cantidad de preguntas \n"))
preguntasCorrectas = int(input("cantidad de preguntas acertadas \n"))

porcentajeCorrectas = cantPreguntas * preguntasCorrectas / 100


if 0.90 <= porcentajeCorrectas:
	print('Nivel Maximo')
elif 0.75 <= porcentajeCorrectas and porcentajeCorrectas < 0.90:
	print('Nivel Medio')
elif 0.50 <= porcentajeCorrectas and porcentajeCorrectas < 0.75:
	print('Nivel Regular')
else:
	print('Fuera de Nivel')


