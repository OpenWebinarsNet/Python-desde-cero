# Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
# sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cad = input("Introduce una cadena:")
while True:
    car = input("Introduce un carácter a buscar:")
    if len(car) == 1: break
while True:
    car_sustituir = input("Introduce un carácter a sustituir:")
    if len(car_sustituir) == 1: break

newcad = cad.replace(car,car_sustituir)

print("La cadena modificada es ",newcad)

