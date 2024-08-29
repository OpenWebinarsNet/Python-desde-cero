# Queremos guardar la temperatura mínima y máxima de 5 días. 
# Realiza un programa que de la siguiente información:

# * La temperatura media de cada día
# * Los días con menos temperatura
# * Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. 
# Si no existe ningún día se muestra un mensaje de información.

# Recorrido para rellenar la tabla (5 días con temp máxima y mínima)
temperaturas = []
for indice in range(1,6):
	temperatura = []
	temperatura.append(int(input("Día %d. Temperatura máxima:" % indice)))
	temperatura.append(int(input("Día %d. Temperatura mínima:" % indice)))
	temperaturas.append(temperatura)

# Mostrar temperatura media
print("Temperaturas medias")
print("===================")

indice = 1
for temperatura in temperaturas:
	print("Día %d. Temperatura media: %f:" % (indice,sum(temperatura)/len(temperatura)))
	indice += 1

# Calcular temperatura mínima más pequeña
# Supongo que es la primera
temp_min = temperaturas[0][1];
for temperatura in temperaturas:
	if temperatura[1] < temp_min:
		temp_min = temperatura[1]

# Mostrar los días con menos temperatura
print("Días con menos temperatura")
print("==========================")
indice = 1
for temperatura in temperaturas:
	if temperatura[1] == temp_min:
		print("Día %d" % indice)
	indice +=1
	
# Días con temperatura máxima
existe_temperatura = False
print("Días con temperatura máxima")
print("===========================")
temp_max = int(input("Introduce una temperatura:"))
indice = 1
for temperatura in temperaturas:
	if temperatura[0] == temp_max:
		print("Día %d" % indice)
		existe_temperatura = True
	indice +=1
if not existe_temperatura:
	print("No hay ningún día con dicha temperatura.")
