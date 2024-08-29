# Queremos guardar los nombres y la edades de los alumnos de un curso. 
# Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre 
# un asterisco (*) Al finalizar se mostrar� los siguientes datos:
#  * Todos lo alumnos mayores de edad.
#  * Los alumnos mayores (los que tienen más edad)

nombres = []
edades = []
# Inicializo las listas hasta que introduzca un "*" 
while True:	
	nombre = input("Dime el nombre de un alumno:")
	if nombre != "*":
		nombres.append(nombre)
		edades.append(int(input("Dime su edad:")))
	if nombre == "*": break;	

# Calcular la edad máxima
edad_max = max(edades)
# Alumnos mayores de edad
print("Alumnos mayores de edad")
print("=======================")
for nombre,edad in zip(nombres,edades):
	if edad >= 18:
		print(nombre)
	
# Alumnos mayores 

print("Alumnos mayores")
print("===============")
for nombre,edad in zip(nombres,edades):
	if edad == edad_max:
		print(nombre)
