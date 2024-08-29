# El director de una escuela está organizando un viaje de estudios, y requiere 
# determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
# viajes por el servicio. La forma de cobrar es la siguiente: 
# si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
# de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
# y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
# sin importar el número de alumnos. 
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses 
# y lo que debe pagar cada alumno por el viaje.

num_alumnos = int(input("¿Cuántos alumnos participan en la actividad?:"))

if num_alumnos>=100:
	coste_por_alumno = 65
if num_alumnos>=50 and num_alumnos<=99:
	coste_por_alumno = 70
if num_alumnos>=30 and num_alumnos<=49:
	coste_por_alumno = 95
if num_alumnos<30 and num_alumnos>0:
	coste_por_alumno = 4000/num_alumnos
if num_alumnos>0:
	coste_autobus = num_alumnos*coste_por_alumno
	print("El coste por alumno es ",coste_por_alumno,"euros.")
	print("El coste del autobús es ",coste_autobus,"euros.")
else:
	print("El número de alumnos debe ser un valor positivo.")


