#A continuación creamos la clase `Persona`. Una persona tendrá un DNI, un #nombre y una edad.
#
#* Creamos el constructor.
#* Crearemos también los métodos seters y getters.
#* Se debe definir el método `mostrar()` para imprimir los datos de la persona.

class Persona():

    def __init__(self,dni,nombre,edad):
        self.dni=dni
        self.nombre=nombre
        self.edad=edad

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self,dni):
        self._dni=dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre	

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self,edad):
        if edad>0:
            self._edad=edad	
        else:
            self._edad=0
            print("Edad incorrecta")

    def mostrar(self):
        return self.dni.mostrar()+" "+self.nombre+" ("+str(self.edad)+")"


