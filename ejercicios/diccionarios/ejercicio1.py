# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas 
# # claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

numero = int(input("Dime un número:"))
cuadrados = {}

for num in range(1,numero+1):
    cuadrados[num] = num ** 2
for num, valor in cuadrados.items():
    print("%d -> %d" % (num,valor))