# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
# y la media de todos los números introducidos.

suma = 0
cont =0

# Con el mientras si el primer número es 0 no va a entrar en el bucle
num=int(input("Número (0 para salir):"))
while num != 0:
	suma = suma + num
	cont = cont + 1
	num=int(input("Número (0 para salir):"))

# Si cont=0 no puedo realizar la división
if cont > 0:
	media = suma / cont
else:
	media = 0

print("Suma:",suma)
print("Media:",media)

