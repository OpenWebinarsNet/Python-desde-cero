#!/usr/bin/env python3
import subprocess
output = subprocess.check_output(["df","-h"])
for fich in output.decode().splitlines()[1:]:
    datos=fich.split(" ")
    while "" in datos:
        datos.remove('')
    print(datos[0]," - ",datos[4])
