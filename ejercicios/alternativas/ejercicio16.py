# La política de cobro de una compañía telefónica es: cuando se realiza una 
# llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
# cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
# los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
# de mañana, 15 %, y en turno de tarde, 10 %. 
# Realice un algoritmo para determinar cuánto debe pagar por cada concepto 
# una persona que realiza una llamada.

tiempo = int(input("¿Cuánto tiempo es la llamada?:"))
es_domingo = input("¿Es Domingo? (S/N):")
if es_domingo.upper() == "N":
	turno = input("¿Qué turno: Mañana o Tarde? (M/T)?:")
if tiempo<5:
	coste = tiempo*100
else:
	if tiempo<8:
		coste = (tiempo-5)*80+500
	else:
		if tiempo<10:
			coste = (tiempo-8)*70+240+500
		else:
			coste = (tiempo-10)*50+140+240+500
if es_domingo.upper() == "S":
	coste = coste+coste*0.03
else:
	if turno.upper() == "M":
		coste = coste+coste*0.15
	else:
		coste = coste+coste*0.10

print("El coste de la llamada: %.2f euros." % (coste/100))
