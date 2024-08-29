# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana
# Para esto, se registran los días que trabajó y las horas de cada día. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores 
# y además calcule cuánto pagó la empresa por los N empleados.

trabajadores = int(input("¿Cuántos trabajadores tiene la empresa?:"))
sueldo_por_hora = float(input("Sueldo por hora:"))
horas_acum = 0
for trabajador in range(1, trabajadores + 1):
	horas_por_trabajador = 0
	dias = int(input("¿Cuántos días ha trabajado el trabajador %d ?:" % trabajador))
	for dia in range(1, dias + 1):
		horas = int(input("¿Cuántas horas ha trabajado el trabajador %d el día %d ?:" % (trabajador,dia)))
		horas_por_trabajador = horas_por_trabajador+horas
	print("El trabajador %d tiene de sueldo %f" % (trabajador,horas_por_trabajador*sueldo_por_hora))
	horas_acum = horas_acum+horas_por_trabajador
print("El pago a los %d trabajadores es: %f" % (trabajadores,horas_acum*sueldo_por_hora))

