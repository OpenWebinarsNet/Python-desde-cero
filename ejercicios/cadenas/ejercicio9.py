# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.

cad = input("Introduce una cadena:")
subcad = input("Introduce una subcadena:")

if cad.find(subcad) > -1:
	print("La cadena contiene la subcadena.")
else:
	print("La cadena no contiene la subcadena.")

# Otra forma de comprobarlo

if subcad in cad:
	print("La cadena contiene la subcadena.")
else:
	print("La cadena no contiene la subcadena.")

