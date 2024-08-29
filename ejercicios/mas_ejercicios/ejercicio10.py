import os
# Procedimiento LeerSecreto: Inicializamos la palabra secreta 
#  y la lista de aciertos a Falso.
# Valores devueltos: Palabra que hay que adivinar, y aciertos: lista
# de valores lógicos que se inicializan a falso indicando que no se han acertado 
# ninguna letra.

def LeerSecreto():
	aciertos = []
	secreto = input("Introduce la palabra a a adivinar:")
	for i in range(len(secreto)):
		aciertos.append(False)
	return secreto,aciertos

# Función NumeroAciertos: Recibe la lista de aciertos y devuelve cuantas letras
# se han acertado (valores Verdadero).
# Parámetro de entrada: aciertos: lista de valores lógicos que indica las letras
# que se han acertado.
# Dato devuelto: Número de letras acertadas

def NumeroAciertos(aciertos):
	return aciertos.count(True)

# Procedimiento EscribirSecreto: Recibe la palabra secreta  
# y la lista de aciertos. Y muestra por pantalla un carácter o un * según la 
# posición del carácter indique en la lista aciertos que se ha acertado la letra 
# (valor Verdadero)
# Parámetro de entrada: Palabra que hay que adivinar, y aciertos: lista de valores 
# lógicos que indica las letras que se han acertado.

def EscribirSecreto(secreto,aciertos):
	# Recorro la cadena de caracteres
	indice = 0
	resultado = ""
	for acierto in aciertos:
		if acierto:
			resultado = resultado + secreto[indice]
		else:
			resultado = resultado + "*"
		indice += 1
	print(resultado)
	
# Función ComprobarSecreto: Recibe un carácter, la cadena a adivinar y la lista 
# de aciertos y devuelve si el carácter está en la cadena. Además si es así cambia
# en la lista aciertos las posiciones donde se encuentra el carácter de Falso a
# Verdadero.
# Parámetro de entrada: un carácter, la cadena y la lista de aciertos
# Dato devuelto: Valor lógico, Verdadero si el carácter está en la cadena, 
# Falso en caso contrario.

def ComprobarSecreto(letra,secreto,aciertos):
	acierto = False
	for i in range(len(secreto)):
		if secreto[i] == letra:
			aciertos[i] = True
			acierto = True
	return acierto,aciertos

# Procedimiento LeerLetra: Lee un carácter por teclado y lo devuelve. Además 
# devuelve un cadena con las letras que se han leído anteriormente.
# Dato de entrada: cadena con todas las letras leídas anteriormente
# Valores devueltos: la letra leída por teclado, y la cadena con todas 
# las letras leídas anteriormente.

def LeerLetra(letras):
	while True:
		letra = input("Introduce una letra:")
		if len(letra)!=1:
			print("Una sola letra!!!")
		else:
			break
	letras = letras + letra + " "
	return letra,letras

# Procedimiento MostarAhorcado: Recibe el número de fallos, y según el valor muestra 
# el nivel de "ahorcamiento" que lleva el jugador.
# Parámetro de entrada: Número de fallos

def MostrarAhorcado(fallos):
	print("")
	print("La horca!!!")
	print("")
	if fallos == 0:
		print("")
		print("")
		print("")
		print("")
		print("")
		print("")
	elif fallos == 1:
		print("")
		print("")
		print("")
		print("")
		print("")
		print("_________")
	elif fallos == 2:
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
		print("_________")
	elif fallos == 3:
		print("------")
		print("|")
		print("|")
		print("|")
		print("|")
		print("_________")
	elif fallos == 4:
		print("------")
		print("|   |")
		print("|   o")
		print("|  ")
		print("|  ")
		print("_________")
	elif fallos == 5:
		print("------")
		print("|   |")
		print("|   o")
		print("|  /|")
		print("|")
		print("_________")
		
	elif fallos == 6:
		print("------")
		print("|   |")
		print("|   o")
		print("|  /|\\")
		print("|")
		print("_________")
	elif fallos == 7:
		print("------")
		print("|   |")
		print("|   o")
		print("|  /|\\")
		print("|  / ")
		print("_________")
	elif fallos == 8:
		print("------")
		print("|   |")
		print("|   o")
		print("|  /|\\")
		print("|  / \\")
		print("_________")
	print("")

# Escribe un programa para jugar al ahorcado.

# Letras: cadena donde se van a ir guardando las letras introducidas
letras = ""
num_fallos = 0
# Se introduce por teclado la palabra secreta a adivinar
secreto,aciertos = LeerSecreto()
# Se repite hasta que el número de aciertos sea igual a la longitud de la palabra o el número de fallos sea 6
while True:
	os.system("clear")
	# Se escribe la palabra (* las letras no acertadas)
	EscribirSecreto(secreto,aciertos);
	
	# Se muestra el dibujo del ahorcado, se haya acertado o no.
	MostrarAhorcado(num_fallos);
	
	# Se muestran las letras que se han introducido anteriormente
	print("Letras introducidas:",letras)
	
	# Se lee una letra y se actualiza las letras leídas
	letra,letras = LeerLetra(letras);
	# Si no hemos acertado la letra mostramos mensaje de error e incrementamos número de fallos.
	acierto, aciertos = ComprobarSecreto(letra,secreto,aciertos)
	if not acierto:
		num_fallos = num_fallos+1;
	if NumeroAciertos(aciertos)==len(secreto) or num_fallos == 8:
		break
	# Podemos salir del bucle por dos razones
	# Si el número de fallos es 6 hemos perdido
	
	
if num_fallos == 8:
	os.system("clear")
	EscribirSecreto(secreto,aciertos);
	MostrarAhorcado(num_fallos);
	print("Has perdido!!!")
else: # Hemos ganado!!!!
	print("Has ganado!!!")
