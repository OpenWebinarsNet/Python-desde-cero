# Función CalcularFactorial: Recibe un número si el número=1 devuelve que el 
# factorial es 1, sino acumula el producto del número con el cálculo del factorial 
# del numero-1. Es una función recursiva.
# Parámetros de entrada: número
# Dato devuelto: Factorial del número

def CalcularFactorial(num):
	if num == 1:
		return 1
	else:
		return num*CalcularFactorial(num-1)
	
# Crear una función recursiva que permita calcular el factorial de un número. 
# Realiza un programa principal donde se lea un entero y se muestre el resultado 
# del factorial.

numero1 = int(input("Número:"))
print("El factorial es:",CalcularFactorial(numero1))
