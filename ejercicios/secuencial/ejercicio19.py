# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: 
# por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en 
# blanco 0. Imprime el resultado obtenido por el estudiante.

correctas = int(input("Dime cantidad de respuestas correctas:"))
incorrectas = int(input("Dime cantidad de respuestas incorrectas:"))
puntos = correctas * 5 + incorrectas * (-1)
print("Puntos:",puntos)
