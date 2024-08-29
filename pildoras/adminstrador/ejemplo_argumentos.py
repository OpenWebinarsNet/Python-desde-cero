#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
	print("Debes poner el usuario como parametro")
	sys.exit(-1)
usuario=sys.argv[1]
fichero=open("/etc/passwd","r")
lineas=fichero.read()
fichero.seek(0)
if lineas.find(usuario)==-1:
	print("Usuario no existe")
elif lineas.find(usuario+":x:0:0")==-1:
	print("No es administrador")
else:
    print("Es administrador")
    for linea in fichero:
        print(linea.split(":")[0])
fichero.close()