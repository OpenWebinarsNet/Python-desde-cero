# Función Intercambiar: Recibe dos números como parámetros de entrada y 
#  devuelve los números ordenador de mayor a menor
# Parámetros de entrada: dos números
# Datos de salida: dos números

def Intercambiar(mayor,menor):
	if mayor<menor:
		return menor,mayor
	else:
		return mayor,menor

# Función CalcularMCD: Recibe dos números y devuelve el MCD utilizando el método 
# de Euclides. El método de Euclides es el siguiente:
#  * Se divide el número mayor entre el menor.
#  * Si la división es exacta, el divisor es el MCD.
#  * Si la división no es exacta, dividimos el divisor entre el resto obtenido y 
# se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# Parámetros de entrada: dos números
# Dato devuelto: El MCD

def CalcularMCD(num1,num2):
	# Se divide el número mayor entre el menor.
	num1, num2 = Intercambiar(num1,num2)
	resto = num1 % num2
	if resto == 0: # Si la división es exacta, el divisor es el MCD.
		return num2
	else:
		# Si la división no es exacta, dividimos el divisor entre el resto obtenido y 
		# se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
		return CalcularMCD(num2,resto)
	
# Crea un programa principal que lea dos números enteros y muestre el MCD.

numero1 = int(input("Número 1:"))
numero2 = int(input("Número 2:"))
print("MCD: ", CalcularMCD(numero1,numero2))
