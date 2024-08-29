# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
fahrenheit = float(input("Introduce la temperatura en ºF:"))
celcius = (fahrenheit - 32) * 5 / 9
print("La temperatura es", celcius, "ºC")
