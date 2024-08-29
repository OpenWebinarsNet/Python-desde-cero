# Una compañía de transporte internacional tiene servicio en algunos países de 
# América del Norte, América Central, América del Sur, Europa y Asia.
# El costo por el servicio de transporte se basa en el peso del paquete 
# y la zona a la que va dirigido...


peso = int(input("¿Qué peso tiene el paquete (en gramos)?:"))
if peso>0 and peso<=5000:
    print("1.- América del Norte")
    print("2.- América Central")
    print("3.- América del Sur")
    print("4.- Europa")
    print("5.- Asia")
    zona = int(input("A que zona se reparte (1-5):"))
    if zona == 1:
        print("Coste:",peso*24, "euros.")
    elif zona == 2:
        print("Coste:",peso*20, "euros.")
    elif zona == 3:
        print("Coste:",peso*21, "euros.")
    elif zona == 4:
        print("Coste:",peso*10, "euros.")
    elif zona == 5:
        print("Coste:",peso*18, "euros.")
    else:
        print("Zona incorrecta.")
else:
    print("Peso incorrecto (no podemos transportar paquetes de más de 5Kg).")

    
