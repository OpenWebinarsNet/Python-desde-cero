# Diseñar el algoritmo correspondiente a un programa, que:
#  * Crea una tabla bidimensional de longitud 5x15 y nombre 'marco'.
#  * Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las 
# posiciones o elementos que delimitan la tabla, es decir, las más externas, 
# mientras que el resto de los elementos contendrán el valor 0.
#  * Visualiza el contenido de la matriz en pantalla.

marco = []
num_filas = 5
num_cols = 15
for indice_fila in range(0,num_filas):
	fila = []
	for indice_col in range(0,num_cols): 
		# Si estoy en el extremo izquierdo, derecho, superior o inferior
		if indice_fila == 0 or indice_fila == num_filas - 1 or indice_col == 0 or indice_col == num_cols -1:
			fila.append(1)
		else:
			fila.append(0)
	marco.append(fila)
# Recorro para mostrar tabla
for fila in marco:
	for elemento in fila:
		print(elemento," ",end="")
	print()

