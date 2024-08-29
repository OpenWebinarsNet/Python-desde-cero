# Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
# divisible por algún otro número.

es_primo = True
numero_es_primo = int(input("Introduce un número para comprobar si es primo:"))
for num in range(2, numero_es_primo):
	if numero_es_primo % num == 0:
		es_primo = False
if es_primo:
	print("Es Primo")
else:
	print("No es Primo")


