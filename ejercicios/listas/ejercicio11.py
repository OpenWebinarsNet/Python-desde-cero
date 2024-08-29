# Diseñar el algoritmo correspondiente a un programa, que:
#  * Crea una tabla bidimensional de longitud 5x5 y nombre 'diagonal'.
#  * Carga la tabla de forma que los componentes pertenecientes a la diagonal de la 
# matriz tomen el valor 1 y el resto el valor 0.
#  * Muestra el contenido de la tabla en pantalla.

matriz = []
for indice_fila in range(0,5):
	fila = []
	for indice_col in range(0,5): 
		# Si estoy en alguna diagonal inicializo a 1
		if indice_fila == indice_col or indice_fila == 4 - indice_col:
			fila.append(1)
		#No estoy en diagonal, inicializo a 0
		else:
			fila.append(0)
	matriz.append(fila)
# Recorro para mostrar tabla
for fila in matriz:
	for elemento in fila:
		print(elemento," ",end="")
	print()
	
