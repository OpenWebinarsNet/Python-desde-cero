# Crea una aplicación que permita adivinar un número. La aplicación genera un 
# número aleatorio del 1 al 100. A continuación va pidiendo números y va 
# respondiendo si el número a adivinar es mayor o menor que el introducido,
# además de los intentos que te quedan (tienes 10 intentos para acertarlo). 
# El programa termina cuando se acierta el número (además te dice en cuantos 
# intentos lo has acertado), si se llega al limite de intentos te muestra el  
# número que había generado.

import random
intentos = 10;
num_secreto  =  random.randint(1,100);
num_ingresado = int(input("Adivine el numero (de 1 a 100):"))

while num_secreto != num_ingresado and intentos>1:
    if num_secreto > num_ingresado:
        print("Muy bajo")
    else: 
        print("Muy alto")
    intentos  =  intentos-1;
    print("Le quedan ",intentos," intentos:")
    num_ingresado = int(input("Adivine el numero (de 1 a 100):"))

if num_secreto == num_ingresado:
    print("Exacto! Usted adivino en ",11-intentos," intentos.")
else:
    print("El numero era: ",num_secreto)

    
