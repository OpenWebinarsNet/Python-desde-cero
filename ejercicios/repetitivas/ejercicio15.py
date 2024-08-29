# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
# euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total 
# de lo que pagó después de los 20 meses.

pago_acum = 0
pago = 10
for mes in range(1, 21):
	pago_acum = pago_acum + pago
	pago = pago * 2
print("Al final de los 20 meses tuvo que pagar: ",pago_acum)

