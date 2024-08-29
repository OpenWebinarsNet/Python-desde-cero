# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

import os
import time
for hora in range(0,24):
	for minuto in range(0,60):
		for segundo in range(0,60):
			os.system("clear")
			print(hora,":",minuto,":",segundo)
			time.sleep(1)
		