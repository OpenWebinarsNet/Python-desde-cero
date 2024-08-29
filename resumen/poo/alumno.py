#Herencia
#
#La clase `Alumno` se hereda de la clase anterior: `Alumno`. 
#Además de los datos de un alumno guardará el curso donde se ha matriculado 
#y una nota. además tendrá un método `estaAprobado()` que dirá si está aprobado según su nota.
#
#* Creamos el constructor.
#* Crearemos también los métodos seters y getters.
#* Se debe definir el método `mostrar()` para imprimir los datos del alumno.

from persona import Persona
class Alumno(Persona):

    def __init__(self,dni,nombre,edad,curso,nota):
        super().__init__(dni,nombre,edad)
        self.curso = curso
        self.nota = nota

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self,curso):
        self._curso=curso

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self,nota):
        if nota >=0 and nota<=10:
            self._nota=nota
        else:
            self._nota=-1
            print("Nota incorrecta")
    
    def estaAprobado(self):
        if self.nota > 5:
            print ("Alumno aprobado")
        elif self.nota>=0 and nota<5:
            print ("Alumno suspendido")
        else:
            print ("Nota incorrecta")
    def mostrar(self):  
        return super().mostrar()+" "+self.curso+" "+str(self.nota)


