# Ejercicio 1/2/3/4/5
'''
class Persona:
#Ejercicio 2
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def set_nombre(self, nombre):
        self.nombre=nombre
    def set_edad(self, edad):
        self.edad=edad

    def get_nombre (self):
        return(self.nombre)
    def get_edad (self):
        return (self.edad)
#Ejercicio 3
    def esMayor (self):
        if self.edad>18:
            mayor=True
        else:
            mayor=False
        return (mayor)
#Ejercicio 4
    def esMayorQue (self, persona):
        if self.edad>persona.edad:
            grande=True
        else:
            grande=False
        return (grande)
#Ejercicio 5    
    @staticmethod
    def get_mayor(persona1, persona2):
        if persona1.edad>persona2.edad:
            elMayor=persona1
        else:
            elMayor=persona2
        return(elMayor)

    def __str__ (self):
        imp = (f"El nombre es {self.nombre} y la edad es {self.edad} años")
        return (imp)

persona1 = Persona ("Jose", 45)
persona2 = Persona ("Maria", 28)
print (persona1)
print (persona2)
print (persona1.esMayor())
print (persona1.esMayorQue(persona2))
perso=Persona.get_mayor(persona1, persona2)
print(f"El mayor: {perso}")
'''
# Ejercicio 6
'''
class alumno:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def aprobado(self):
        if self.nota>10 or self.nota<0:
            eval=("Nota erronea")
        elif self.nota>=9:
            eval=("Excelente")
        elif self.nota>=6 and self.nota<9:
            eval=("Aprobado")
        elif self.nota>=4 and self.nota<6:
            eval=("Desaprobado")
        else:
            eval=("Aplazado")
        return (eval)

    def __str__(self):
        imp=(f"El nombre del alumno es {self.nombre}")
        return (imp)

alumn1 = alumno("Jose Perez", 11)
alumn2 = alumno("Carina Paz", 9)
alumn3 = alumno("Roque Choque", 4)

print(alumn1)
print(alumn2)
print(alumn3)
print(alumn1.aprobado())
print(alumn2.aprobado())
print(alumn3.aprobado())
'''
# Ejercicio 7
'''
class Triangulo:
    def __init__(self, l1, l2, l3):
        self.lado1=l1
        self.lado2=l2
        self.lado3=l3

    def __str__(self):
        imp=(f"El primer lado es {self.lado1}, el segundo lado es {self.lado2} y el tercero es {self.lado3}")
        return(imp)

    def ladoMayor(self):
        if self.lado1>self.lado2:
            if self.lado1>self.lado3:
                mayor=self.lado1
            else:
                mayor=self.lado3
        else:
            if self.lado2>self.lado3:
                mayor=self.lado2
            else:
                mayor=self.lado3
        return (mayor)

    def tipoTriangulo(self):
        if self.lado1==self.lado2==self.lado3:
            tipo=("Equilatero")
        elif self.lado1==self.lado2 or self.lado1==self.lado3 or self.lado2==self.lado3:
            tipo=("Isoceles")
        else:
            tipo=("Escaleno")
        return(tipo)
            

listaLados = [0, 0, 0]
lar=len(listaLados)
for i in range(lar):
    listaLados[i]=int(input("Ingrese un lado: ")) 

l1=listaLados[0]
l2=listaLados[1]
l3=listaLados[2]
print(l1, l2, l3)

tria= Triangulo(l1, l2, l3)
print(tria.ladoMayor())
print(tria.tipoTriangulo())
print(tria)
'''
# Ejercicio 8
'''
class Calculadora:
    

    def __init__(self, x=0, y=0): #Declaro los valores por defecto.
        self.x=int(input("Ingrese el valor de X: "))
        self.y=int(input("Ingrese el valor de Y: "))

    def __str__(self):
        return (self.x, self.y)
    
    def suma(self):
        resSum=self.x+self.y
        return (resSum)

    def resta(self):
        resRest=self.x-self.y
        return(resRest)
    
    def multiplicacion(self):
        resMult=self.x*self.y
        return (resMult)
    
    def division(self):
        resDiv=""
        if self.y==0:
            resDiv=("error, no se puede dividir por cero")
        else:
            resDiv=self.x/self.y
        return (resDiv)
    

calc=Calculadora()
print(calc.x, calc.y)

print(f"La suma de {calc.x} y {calc.y} es {calc.suma()} la resta es {calc.resta()}.\
 4 Su multiplicacion es {calc.multiplicacion()} y la division es {calc.division()}")
'''
# Ejercicio 9
'''
class Agenda:
    def __init__(self, contacto):
        self.contacto = []
        #self.contacto.append(contacto)

    def agregar(self, nuevoContacto):
        self.contacto.append(nuevoContacto)

    def buscarContacto(self, nombre):
        largo = (len(self.contacto))
        noEncontrado = False
        for i in range(largo):
            contactoCargado = self.contacto[i]
            if contactoCargado[0] == nombre:
                print(contactoCargado)
                noEncontrado = False  # Si encontramos el contacto en algun momento
            else:
                noEncontrado = True  # Si no se encuentra el contacto
        if noEncontrado:
            print("No se encontro el contacto",)

    def editarContacto(self, nuevoContacto, nombre):
        largo = (len(self.contacto))
        noEncontrado = False
        for i in range(largo):
            contactoCargado = self.contacto[i]
            if contactoCargado[0] == nombre:
                index = i
                self.contacto[i] = nuevoContacto
                noEncontrado = False
            else:
                noEncontrado = True
        if noEncontrado:
            ingreso = input("No se encontro el contacto, ingrese 1 para agregar nuevo contacto\
ingrese cualquier otra cosa para ignorar ")
            if ingreso == "1":
                self.contacto.append(nuevoContacto)

    def listar(self):
        largo = len(self.contacto)
        for i in range(largo):
            print(self.contacto[i])
        print(len(contacto))


#
#ncontacto = ["Emiliano Vazques", "123412341234", "EVasquez@gmail.com"]
contacto=[]
agen = Agenda(contacto)
#agen.agregar(ncontacto)


cerrar = False
while cerrar != True:
    opcion = input("\n\n Ingrese una opcion:\n 1) Para agregar un contacto\n 2) Para listar los contactos\n \
3) Para buscar un contacto\n 4) Para editar un contacto\n 5) Para salir\n Ingrese la opcion deseada: ")
    if opcion == "1":  # Agregar nuevo contacto
        nuevoContacto = ["", "", ""]
        nuevoContacto[0] = input("Ingrese el nombre: ")
        nuevoContacto[1] = input("Ingrese el telefono: ")
        nuevoContacto[2] = input("Ingrese el email: ")
        agen.agregar(nuevoContacto)
    elif opcion == "2":  # TODOS los contactos
        agen.listar()
    elif opcion == "3":
        nombre = input("Ingrese el nombre a buscar: ")
        agen.buscarContacto(nombre)
    elif opcion == "4":
        nombre = input("Ingrese el nombre a editar: ")
        nuevoContacto = ["", "", ""]
        nuevoContacto[0] = input("Ingrese el nuevo nombre: ")
        nuevoContacto[1] = input("Ingrese el nuevo telefono: ")
        nuevoContacto[2] = input("Ingrese el nuevo email: ")
        agen.editarContacto(nuevoContacto, nombre)  
    elif opcion == "5":
        print("Que tenga un buen día")
        cerrar = True   
    else:
        print("Opcion no reconocida")
'''
