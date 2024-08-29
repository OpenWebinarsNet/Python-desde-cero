# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
# y la media de todos los números introducidos.

suma = 0
cont =0
while True:
	num=int(input("Número (0 para salir):"))
	suma = suma + num
	# Si num=0 no debemos tenerlo en cuenta para calcular la media
	if num !=0:
		cont = cont + 1
	if num == 0:
		break
# Si cont=0 no puedo realizar la división
if cont != 0:
	media = suma / cont
else:
	media = 0

print("Suma:",suma)
print("Media:",media)