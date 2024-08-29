# Función CalcularVuelta: Recibe el dinero que hay que devolver y el valor de un
# billete o una moneda, devuelve el número de billetes o monedas de esa cantidad
# que hay que devolver y actualiza el dinero que queda por devolver.
# Parámetros de entrada: cantidad: valor del billete o la moneda
# Dato devuelto: vuelta: Número de billetes o monedas que hay que devolver y
# cantidad que queda por devolver

def CalcularVuelta(dinero, cantidad):
	# Realizamos la división entera entre el dinero
	# que hay que devolver y la cantidad del billete o moneda
	vuelta = dinero // cantidad
	# Actualizamos el dinero que queda por devolver
	dinero = dinero - vuelta*cantidad
	return vuelta, dinero

# Función InicializaBilletesMonedas: Recibe un vector "cantidades" donde
# vamos a guardar el valor de los billetes y monedas de mayor a menor.
# Valor devuelto : cantidades

def InicializaBilletesMonedas():
    cantidades = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    return cantidades

# Función EscribirVuelta: Recibe la cantidad de billetes o monedas y su valor
# y los imprime por pantalla. Se imprime si hay que devolver de ese billete o moneda
# es decir, si la vuelta>0. Si la cantidad>2 se devuelven billetes (euros),
# sino se devuelven monedas y si la cantidad es >=1 se devuelven euros, sino céntimos.
# Parámetros de entrada: vuelta: cantidad de billetes o monedas a devolver y
# cantidad: valor del billete o moneda

def EscribirVuelta(vuelta,cantidad):
	# Se imprime si hay algo que devolver
	if vuelta>0:
		# Si la cantidad es menor de 2 devolvemos billetes
		if cantidad>2:
			print(vuelta, " billetes de ",cantidad," euros.")
		else:
			# SiNo devolvemos monedas
			# Si la cantidad>=1 devolvemos euros
			if cantidad>=1:
				print(vuelta, " monedas de ",cantidad," euros.")
			else: # Devolvemos céntimos (lo multiplicamos por 100)
				print(vuelta, " monedas de ",cantidad*100," céntimos.")

# Realizar una aplicación que recoja por teclado la cantidad total a pagar y la
# cantidad que se ha entregado. La aplicación debe calcular el cambio
# correspondiente con el menor número de monedas y/o billetes posibles.

total = float(input("Dinero a pagar:"))
entregada = float(input("Dinero pagado:"))
dinero = entregada-total
# Incializamos las cantidades de billetes o monedas
cantidades = InicializaBilletesMonedas()
# Por cada cantidad, calculamos la vuelta e imprimimos lo que hay que devolver
for indice in range(15):
    vuelta, dinero = CalcularVuelta(dinero,cantidades[indice])
    EscribirVuelta(vuelta,cantidades[indice])
