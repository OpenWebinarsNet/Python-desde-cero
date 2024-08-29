# Si tenemos una cadena con un nombre y apellidos, realizar un programa que 
# muestre las iniciales en mayúsculas.

iniciales = ""
posicion=0
cad = input("Introduce una cadena:")

# Elimino los posible espacios que haya al principio y final de la cadena
cad = cad.strip()
# La primera inicial es la primera letra de la primera palabra
iniciales = iniciales + cad[0]

# Voy buscando los espacios
posicion = cad.find(" ", posicion)
while  posicion != -1:
	# No tengo en cuanta los posibles espacios que haya entre las palabras
	while cad[posicion + 1] == " ":
		posicion = posicion + 1
	iniciales = iniciales + cad[posicion +1]
	posicion = cad.find(" ", posicion + 1)

print("Iniciales:",iniciales.upper())

