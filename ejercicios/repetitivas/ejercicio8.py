# Escribe un programa que pida el limite inferior y superior de un intervalo. 
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. 
# Cuando termine el programa dará las siguientes informaciones:
# 	* La suma de los números que están dentro del intervalo (intervalo abierto).
# 	* Cuantos números están fuera del intervalo.
# 	* He informa si hemos introducido algún número igual a los límites del intervalo.

suma_dentro_intervalo = 0
cont_fuera_intervalo = 0
igual_limites = False
# Me aseguro que el lim_inf es menor que el lim_sup
while True:
	lim_inf = int(input("Introduce el límite inferior del intervalo:"))
	lim_sup = int(input("Introduce el límite superior del intervalo:"))
	if lim_inf>lim_sup:
		print("ERROR: El límite inferior debe ser menor que el superior.")
	if lim_inf<=lim_sup:
		break;

num = int(input("Introduce un número (0, para salir):"))
while num !=0:
	# Pertenece al intervalo
	if num>lim_inf and num<lim_sup:
		suma_dentro_intervalo = suma_dentro_intervalo + num
	else:
		# No pertenece al intervalo
		cont_fuera_intervalo = cont_fuera_intervalo + 1
	
	# Número igual a alguno de los límites
	if num == lim_inf or num == lim_sup:
		igual_limites = True
	
	num = int(input("Introduce un número (0, para salir):"))

print("La suma de los número dentro del intervalo es ",suma_dentro_intervalo)
print("La cantidad de números fuera del intervalo es ",cont_fuera_intervalo)
if igual_limites:
	print("Se ha introducido algún número igual a los límites del intervalo.")
else:
	print("No se ha introducido ningún número igual a los límites del intervalo.")
