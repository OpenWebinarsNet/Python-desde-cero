# Un alumno desea saber cual será su calificación final en la materia de Algoritmos
# Dicha calificación se compone de los siguientes porcentajes:
# * 55% del promedio de sus tres calificaciones parciales.
# * 30% de la calificación del examen final.
# * 15% de la calificación de un trabajo final.

parcial1 = float(input("Dime la nota del parcial 1:"))
parcial2 = float(input("Dime la nota del parcial 2:"))
parcial3 = float(input("Dime la nota del parcial 3:"))
examen = float(input("Dime la nota del examen:"))
trabajo = float(input("Dime la nota del trabajo:"))
nota = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + 0.3 * examen + 0.15 * trabajo
print("nota final:", nota)

