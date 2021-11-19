class Persona:
    def __init__(self, d,n,a):
        self.documento=d
        self.nombre=n
        self.apellido=a
    def __str__(self):  
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Doc:{self.documento}"

class Alumno(Persona):             # La clase Alumno hereda de Persona
    def __init__(self,d,n,a,c):
        super().__init__(d,n,a)    # asignando atributos al constructor de la clase Persona 
        self.curso=c   


    def __str__(self):
        return super().__str__() +f" Curso: {self.curso}"	# estoy usando el metodo __str__  
	                                                        # de  la clase padre (superclase)
								# y le estoy agregando que tambien
       		                                                # muestre el atributo curso
class Docente(Persona):
    def __init__(self,d,n,a,l):
        super().__init__(d,n,a)
        self.legajo=l
    def __str__(self):
        return super().__str__() + f" Legajo: {self.legajo}" 

#programa principal                                                         
p=Persona(123,"Nora","Paz")                                
print(p)    
a=Alumno(1111,"Juan","Guerra",2126)
print(a)
d=Docente(456,"Marcela","Apellido",4444)
print(d)