# Crea un programa que pida un número al usuario un número de mes 
# (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) 
# y el nombre del mes. Debes usar listas. Para simplificarlo vamos 
# a suponer que febrero tiene 28 días.

dias = [31,28,31,30,31,30,31,31,30,31,30,31]
nombre_mes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
while True:
	mes = int(input("Introduce un mes (1-12):"))
	if mes < 1 or mes > 12:
		print("Error: mes incorrecto.")
	if mes>=1 and mes<=12: break
print("El mes de",nombre_mes[mes-1],"tiene",dias[mes-1],"días.")
