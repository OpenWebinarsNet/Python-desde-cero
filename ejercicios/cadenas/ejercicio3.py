# Pide una cadena y un carácter por teclado (valida que sea un carácter) 
# y muestra cuantas veces aparece el carácter en la cadena.

cad = input("Introduce una cadena:")
while True:
    car = input("Introduce un carácter:")
    if len(car) == 1: break

print("En la cadena",cad,"aparecen",cad.count(car),"veces el carácter",car)