# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas 
# por una empresa en sus 4 sucursales. Informar:
#  * Las cantidades totales de cada articulo.
#  * La cantidad de artículos en la sucursal 2.
#  * La cantidad del articulo 3 en la sucursal 1.
#  * La recaudación total de cada sucursal.
#  * La recaudación total de la empresa.
#  * La sucursal de mayor recaudación.


precios = []
cantidades = []
num_articulos = 5
num_sucursales = 3
# Leer Precios
for indice_art in range(0, num_articulos):
   precios.append(float(input('Ingrese Precio Articulo %d:' % (indice_art+1))))

# Leer Cantidades


for indice_sucursal in range(0, num_sucursales):
    cant_art = []
    for indice_art in range(0, num_articulos):
        cant_art.append(int(input('Ingrese Cant. de Articulo %d, en sucursal %d:' % (indice_art+1,indice_sucursal+1))))
    cantidades.append(cant_art)
   
## Sumar cantidades por artículos
print('Cantidades por artículos:')
for indice_art in range(0, num_articulos):
    suma = 0
    for cant_sucursal in cantidades:
        suma = suma + cant_sucursal[indice_art]
    print('Total articulo %d: %d' % (indice_art + 1,suma))

# Informar Total de artículos Sucursal 2

print('Total Sucursal 2: %d' % sum(cantidades[1]))

# Informar Sucursal 1, Articulo 3:
print('Sucursal 1, Articulo 3: %d' % cantidades[0][2])

# Guardo en una lista las recaudaciones de cada sucursal
total_por_sucursal = []
for precio,cant_sucursal in zip(precios,cantidades):
    total_por_sucursal.append(sum(cant_sucursal) * precio)
# Calculo el máximo que se ha vendido
mayorrec = max(total_por_sucursal)   
indice_sucursal = 1
for cant_sucursal in cantidades:
    print('Recaudaciones Sucursal %d: %f' % (indice_sucursal,sum(cant_sucursal)))
    indice_sucursal += 1

# Calculo la sucursal con mayor recaudación
indice_sucursal = 1
for cant_sucursal in total_por_sucursal:
    if cant_sucursal == mayorrec: break
    indice_sucursal += 1

print('Recaudación total de la empresa: %f' % sum(total_por_sucursal))
print('Sucursal de Mayor Recaudación: %d' % indice_sucursal)


