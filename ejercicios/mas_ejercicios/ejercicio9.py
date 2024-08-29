import random
import os
# Función EstaRepetido: Recibe un número y una lista de cuatro números y comprueba
#  si el número no está en la lista.
# Parámetro de entrada: Número y vector
# Dato devuelto: Valor lógico: Verdadero si el número está en la lista y falso si no.

def EstaRepetido(num,vector):
	return num in vector

# Procedimiento GenerarSecuencia: Recibe una lista que se inicializa con 4 enteros 
# no repetidos
# Dato devuelto: Lista de 4 enteros

def GenerarSecuencia():
	vector = []
	while True:
		num = random.randint(0,9)
		if num not in vector:
			vector.append(num)
		if len(vector)==4:
			break
	return vector
	

# Procedimiento LeerSecuencia: Recibe una lista que se inicializa con 4 enteros 
# leídos por teclado por el usuario, asegurando de que no se introduce ninguno 
# repetido.
# Dato devuelto: Lista de 4 enteros

def LeerSecuencia():
	vector = []
	while True:
		num = int(input("Número:"))
		if num not in vector:
			vector.append(num)
		else:
			print("No debes indicar números repetidos.")
		if len(vector)==4:
			break
	return vector
	

# Procedimiento ComprobarSecuencia: Recibe dos vectores, el secreto y el introducido
# por el usuario y devuelve el número de coincidencias en la misma posición (muertos)
#  y las coincidencias en distintas posición (heridos).
# Parámetros de entrada: Dos vectores
# Dato devuelto: muertos y heridos

def ComprobarSecuencia(secreto,usuario):
	m = 0
	h = 0
	# recorro los dos vectores
	for indice_secreto in range(0,len(secreto)):
		for indice_usuario in range(0,len(usuario)):
			if secreto[indice_secreto] == usuario[indice_usuario]:
				# Si el elemento coincide y además están en la misma posición, incremento los muertos.
				if indice_secreto == indice_usuario:
					m = m + 1
				else:
					# Si el elemento coincide pero no están en la misma posición, incremento los heridos.
					h = h + 1
	return m,h
			
# Vamos a programar el juego "Mastermind", para ello el programa debe "eligir" un 
# número de cuatro cifras (sin cifras repetidas), que será el código que el jugador 
# debe adivinar en la menor cantidad de intentos posibles. Cada intento consiste en 
# una propuesta de un código posible que escribe el jugador, y una respuesta del 
# programa. Las respuestas le darán pistas al jugador para que pueda deducir el código.
#  * Número de "MUERTOS": Es la cantidad de dígitos que están en el número secreto 
# y en la misma posición,
#  * Número de "HERIDOS:" Es la cantidad de dígitos que están en el número secreto 
# pero no en la misma posición.
resultados = []
# Se genera el número secreto a adivinar
secreto = GenerarSecuencia()
# Se repeti hasta que se acierte, número de muertos = 4
while True:
	# Leemos la secuencia propuesta por el usuario
	usuario = LeerSecuencia()
	muertos = 0
	heridos = 0
	# Se comprueba la propuesta
	muertos, heridos = ComprobarSecuencia(secreto,usuario)
	# Voy a guardar el numero, con el resultado
	numero = ""
	for num in usuario:
		numero = numero + str(num)
	# Y se imprimen los muertos y heridos
	resultados.append(numero+" - MUERTOS: "+str(muertos)+" - HERIDOS: "+str(heridos))
	# Muestro los resultados
	os.system("clear")
	for resultado in resultados:
		print(resultado)
	if muertos == 4:
		break	
	