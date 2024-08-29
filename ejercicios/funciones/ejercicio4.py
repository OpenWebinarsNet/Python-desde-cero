# Función ConvetirEspaciado: Recibe una cadena de caracteres, y devuelve otra 
# con los mismos caracteres separados con espacio.
# Parámetros de entrada: Cadena de caracteres
# Dato devuelto: Cadena igual a la anterior pero con espacios entre los 
# caracteres

def ConvertirEspaciado(cad):
	cad_con_espacio = cad.replace(""," ")
	cad_con_espacio.strip()
	return cad_con_espacio

# Crea un función "ConvertirEspaciado", que reciba como parámetro un texto y 
# devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, 
# "Hola, tú" devolverá "H o l a , t ú ". Crea un programa principal donde se 
# use dicha función.

mensaje = input("Introduce una cadena:")
print("La cadena con espacio:",ConvertirEspaciado(mensaje))
