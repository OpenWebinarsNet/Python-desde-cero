# Función Login: Recibe un nombre de usuario y una contraseña, y devuelve un
# valor lógico: verdadero si se ha introducido el nombre y la contraseña adecuadas.
# Además devuelve el numero de internos 
# Parámetros de entrada: nombre y contraseña, y el número de intentos actual
# Datos devueltos: Valor lógico indicando si ha hecho login, e intentos

def Login(nombre,password,intentos):
	intentos += 1
	if nombre == "usuario1" and password == "asdasd":
		return(True,intentos)
	else:
		return(False,intentos)
		
# Crear una subrutina llamada "Login", que recibe un nombre de usuario y una 
# contraseña y te devuelve Verdadero si el nombre de usuario es "usuario1" y la 
# contraseña es "asdasd". Además recibe el número de intentos que se ha intentado 
# hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña 
# y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.


cuantasveces = 0
while True:
	usuario = input("Usuario:")
	clave = input("Password:")
	entrar,cuantasveces = Login(usuario,clave,cuantasveces)
	if not entrar:
		print("Error. Nombre de usuario o contraseña incorrecta.")
	if entrar or cuantasveces == 3: 
		break
	# Sale si he hecho login o llego a los tres intentos
	# Puedo llegar a esta instrucción por dos razones
	# Si he hecho login muestro mensaje de bienvenida
if entrar:
	print("Bienvenidos al sistema")
else: # He llegado a los tres intentos
	print("No has entrado en el sistema")
