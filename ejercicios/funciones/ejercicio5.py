# Procedimiento CalcularMaxMin: recibe una lista de enteros  y devuelve
#  el máximo y el mínimo de los números guardados en el vector.
# Parámetros de entrada: lista de enteros
# Valores de salida: valor máximo y mínimo
import random
def CalcularMaxMin(lista):
	return (max(lista),min(lista))

# Crea una función "calcularMaxMin" que recibe una lista con valores numéricos y 
# devuelve el valor máximo y el mínimo. Crea un programa que pida números por 
# teclado y muestre el máximo y el mínimo, utilizando la función anterior.

numeros = []
# Incializo la lista con valores aleatorios
for i in range(10):
	numeros.append(random.randint(1,100))
vmax,vmin = CalcularMaxMin(numeros)
print("El valor máximo es ",vmax)
print("El valor mínimo es ",vmin)
