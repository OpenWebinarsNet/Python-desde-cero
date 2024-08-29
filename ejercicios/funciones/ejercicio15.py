# Función LongitudCola: Recibe una lista (cola).
# Devuelve un contador con los elementos de la cola.

def LongitudCola(cola):
	return len(cola)

# Función EstaVaciaCola: Recibe una lista (cola).
# Devuelve un valor lógico indicando si la cola está vacía.

def EstaVaciaCola(cola):
	return len(cola) == 0

#Procedimiento AddCola: Recibe una lista (cola) y un elemento (cadena)
# Parámetro de entrada:La cola y el elemento.
# Valor devuelto: La cola
def AddCola(cad, cola):
	cola.append(cad)

#Función SacarCola: Recibe una lista (cola) y devuelve 
# el elemento que se ha introducido en primer lugar, si no está vacía.
# Si está vacía, escribe un mensaje de error.
# Parámetro de entrada:La cola y el elemento.
# Dato devuelto: El elemento 
def SacarDeLaCola(cola):
	if not EstaVaciaCola(cola):
		return cola.pop(0)
	else:
		print("No se puede sacar elemento. La cola está vacia")
		return ""
		

# Función EscribirCola: Recibe una lista (cola).
# Muestra los elementos de la cola.
# Parámetros de entrada: La cola
def EscribirCola(cola):
	for elem in cola:
		print(elem,end=" ")
	print()
		

# Realiza un programa principal que nos permita usar funciones para manipular pilas.
micola = []
while True:
	print("1.- Añadir elemento a la cola")
	print("2.- Sacar elemento de la cola")
	print("3.- Longitud de la cola")
	print("4.- Mostrar cola")
	print("5.- Salir")
	opcion = int(input())
	if opcion == 1:
		elem = input("Dame la cadena para añadir a la cola:")
		AddCola(elem,micola)
	elif opcion == 2:
		print(SacarDeLaCola(micola))
	elif opcion == 3:
		print("Longitud: ",LongitudCola(micola))
	elif opcion == 4:
		EscribirCola(micola)
	elif opcion == 5:
		break
	else:
		print("Opción incorrecta")
	