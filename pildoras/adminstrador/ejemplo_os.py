#!/usr/bin/python3
import os
# Descubrir nuestro directorio de trabajo actual
dirActual = os.getcwd()
print("Directorio trabajo actual: {}".format(dirActual))

# Crear un directorio si este no existe
##Pedimos el path del directorio a crear:
carpeta = str(input("\nIntroduce directorio a crear (ruta completa): "))
##Primero comprobamos si esta ya existe
if os.path.exists(carpeta):   # Si queremos ver si existe y es un directorio: os.path.isdir(carpeta)
    print("La carpeta {} ya existe".format(carpeta))
    exit(1)
else:
    os.system("mkdir {}".format(carpeta))
    print("Creamos la carpeta {}".format(carpeta))
    # Para ver un listado del directorio donde se creó ahora mismo esa carpeta
    cpath = carpeta.split("/")[0:-1] #Seleccionamos todas menos la creada
    dir_madre = os.sep.join(cpath) #Que, en el caso de linux es "/".join(cpath)
    print("Directorio madre : {}".format(dir_madre))
    listado = os.listdir(dir_madre)
    print("listado de los elementos de {}:".format(dir_madre))
    for elemento in listado:
        print(" - {}".format(str(elemento)))
exit(0)
