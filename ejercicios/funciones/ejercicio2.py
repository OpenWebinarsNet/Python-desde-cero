# Función EsMultiplo: Recibe dos número e indica si el primero el múltiplo del 
# segundo. Para ello calculo el resto de la división, si es 0 es múltiplo.
# Parámetros de entrada: dos números
# Dato devuelto: múltiplo: Valor lógico verdadero si el primero es múltiplo 
# del segundo, Falso en caso contrario.

def esmultiplo(num1,num2):
	if num1 % num2 == 0:
		return True
	else:
		return False

# Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos 
# es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, 
# y devuelve si el primero es múltiplo del segundo.

numero1 = int(input("Número 1:"))
numero2 = int(input("Número 2:"))
if esmultiplo(numero1,numero2):
	print(numero1,"es múltiplo de",numero2)
else:
	print(numero1,"no es múltiplo de",numero2)
