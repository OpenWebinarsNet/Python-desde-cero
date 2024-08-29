# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos 
# circunferencias y las clasifique en uno de estos estados:
# exteriores
# tangentes exteriores
# secantes
# tangentes interiores
# interiores
# concéntricas

import math

x1 = float(input("Dime coordenada x primera circunferencia:"))
y1 = float(input("Dime coordenada y primera circunferencia:"))
r1 = float(input("Dime radio primera circunferencia:"))
x2 = float(input("Dime coordenada x segunda circunferencia:"))
y2 = float(input("Dime coordenada y segunda circunferencia:"))
r2 = float(input("Dime radio segunda circunferencia:"))


distancia = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
#  circunferencias exteriores
# La distancia entre los centros, d, es mayor que la suma de los radios.
if distancia > (r1 + r2):
	print("Circunferencias exteriores")
#  circunferencias tangentes exteriores
# La distancia entre los centros es igual a la suma de los radios.
if distancia == (r1 + r2):
	print("Circunferencias tangentes exteriores")
#  circunferencias secantes
# La distancia  es menor que la suma de los radios y mayor que su diferencia.
if distancia < (r1 + r2) and distancia > abs(r1-r2):
	print("Circunferencias secantes")
#  Circunferencias tangentes interiores
# La distancia entre los centros es igual a la diferencia entre los radios.
if distancia == abs(r1-r2):
	print("Circunferencias tangentes interiores")
#  Circunferencias interiores
# La distancia entre los centros es mayor que cero y menor que la diferencia entre los radios. 
if distancia>0 and distancia<abs(r1-r2):
	print("Circunferencias interiores")
#  Circunferencias concétricas
#  La distancia = 0.
if distancia == 0:
	print("Circunferencias concétricas")
