

# Crear un programa que convierta un número entero (mayor que 1 y menor o igual
# que 1000) a número romano.
# Análisis
# Inicializamos 3 vectores de 10 elementos, con los números romanos correspondientes
# a las unidades, decenas y centenas.
# Calculamos el número de centenas que tiene el número, y mostramos el número romano
# Calculamos el número de decenas que tiene el número, y mostramos el número romano
# Calculamos el número de unidades que tiene el número, y mostramos el número romano

# Inicializamos 3 listas, con los números romanos correspondientes
# a las unidades, decenas y centenas.
nu = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
nd = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
nc = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
#  leer el número
while True:
    num = int(input("Ingrese un número entre 1 y 1000:"))
    if num>0 and num<=1000:
        break
# Si el numero es 1000 mostramos el número romano M
if num == 1000:
    print("M")
else:
    # Calculamos las centenas,decenas y unidades.
    centenas = num // 100
    decenas = (num // 10) % 10
    unidades = num % 10
    # Mostramos los números romanos correspondientes.
    print(nc[centenas],nd[decenas],nu[unidades])
