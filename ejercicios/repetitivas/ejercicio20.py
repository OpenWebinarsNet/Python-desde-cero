# Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
# de números primos que queremos mostrar.

import math
while True:
    cant_a_mostrar = int(input("Ingrese la cantidad de números primos a mostrar:"))
    if cant_a_mostrar>0: break

print("1 :  2") # el primer primo es 2, los otros son todos impares...
cant_mostrados = 1
num = 3            # ...a partir de 3

while cant_mostrados < cant_a_mostrar:
    es_primo = True # pienso que es primo hasta que encuentre con que dividirlo
    for divisor in range(3, int(math.sqrt(num)) + 1, 2): # ya sabemos que es impar
        if num % divisor == 0: # si la divisi�n da exacta...
            es_primo = False  # ...ya no es primo

    if es_primo:
        cant_mostrados = cant_mostrados + 1
        print(cant_mostrados, ": ",num)
    num = num + 2 


