# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el 
# número invertido.

num = int(input("Dime un número de dos cifras:"))
decenas = num // 10
unidades = num % 10
print("Primera cifra (decenas):",decenas)
print("Segunda cifra (unidades):",unidades)