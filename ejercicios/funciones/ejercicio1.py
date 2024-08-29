# Función centrar: Recibe una cadena y la imprime centrada en la pantalla.
# Suponemos que tenemos una pantalla de 80 caracteres de ancho. 
# Para centrar usamos la formula 40 - (Longitud(cad)/2)
# Parámetros de entrada: cadena a imprimir centrada


def centrar(cad):
	print(" " * int(40 - (len(cad)/2)),cad)
	print(" " * int(40 - (len(cad)/2)),"=" * len(cad))


# Crea un función EscribirCentrado, que reciba como parámetro un texto y lo 
# escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: 
# deberás escribir 40 - longitud/2 espacios antes del texto). 
# Además subraya el mensaje utilizando el carácter =.

mensaje1 = "Un mensaje centrado"
centrar(mensaje1)
mensaje2 = "Otro mensaje"
centrar(mensaje2)

	
