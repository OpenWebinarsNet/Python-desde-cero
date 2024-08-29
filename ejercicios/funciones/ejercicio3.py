# Función calcularTemperaturaMedia: Recibe dos números reales que representan 
# dos temperaturas y devuelve la temperatura media.
# Parámetros de entrada: dos temperaturas (real)
# Dato devuelto: La temperatura media (real)

def calcularTemperaturaMedia(temp1,temp2):
	return (temp1 + temp2)/2

# Crear una función que calcule la temperatura media de un día a partir de la 
# temperatura máxima y mínima. Crear un programa principal, que utilizando la 
# función anterior, vaya pidiendo la temperatura máxima y mínima de cada día 
# y vaya mostrando la media. El programa pedirá el número de días que se van 
# a introducir.

cantidad=int(input("¿Cuántas temperaturas vas a calcular?:"))
for indice in range(cantidad):
	tmin = float(input("Introduce temperatura mínima:"))
	tmax = float(input("Introduce temperatura máxima:"))
	print("Temperatura media:",calcularTemperaturaMedia(tmin,tmax))
