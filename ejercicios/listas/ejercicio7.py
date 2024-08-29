# Programa que declare tres listas 'lista1', 'lista2' y 'lista3' de cinco 
# enteros cada uno, pida valores para 'lista1' y 'lista2' y 
# calcule lista3=lista1+lista2.

lista1 = []
lista2 = []
lista3 = []
for indice in range(1,6):
	lista1.append(int(input("Introduce el elemento %d del vector1:" % indice)))
for indice in range(1,6):
	lista2.append(int(input("Introduce el elemento %d del vector2:" % indice)))

for indice in range(0,5):
	lista3.append(lista1[indice] + lista2[indice])

print("La suma de los vectores es:")
for numero in lista3:
	print(numero," ",end="")
