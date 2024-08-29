# Realizar una algoritmo que muestre la tabla de multiplicar de un número 
# introducido por teclado.

tabla = int(input("¿De qué número quieres mostrar la tabla de multiplicar?:"))
for num in range(1, 11):
	print("%d * %d = %d" % (num,tabla,num*tabla))
