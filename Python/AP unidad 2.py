# Ejercicio 1
'''
def mayor(x, y ,z):
    if x>0 and y>0 and z>0:
        max=0
        if x>y:
            if x>z:
                max=x
            else:
                max=z
        else:
            if y>z:
                max=y
            else:
                max=z
    return(max)

x=int(input("Ingrese el primer numero: "))
y=int(input("Ingrese el segundo numero: "))
z=int(input("Ingrese el tercer numero: "))
print(mayor(x,y,z))
'''
# Ejercicio 2
'''
def fechaCorrecta(d,m,a):
    fecha=True
    if d>0 and m>0 and a>=0: #Nos aseguramos que todos sean numeros positivos 
        if m<1 and m>12:    #Descartamos que los meses esten fuera de rango
            fecha=False
        elif m==2:
            if d>29:    #Maximo rango de febrero
                fecha=False
        elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if d>31:
                fecha=False
        else:
            if d>30:
                fecha:False
    else:       #Salida si algun numero es negativo
        fecha=False
    return (fecha)

d=int(input("Ingrese el día: "))
m=int(input("Ingrese el mes: "))
a=int(input("Ingrese el año: "))
print(fechaCorrecta(d,m,a))
'''
# Ejercicio 3
'''
def vuelto(totComp, billetes):
    vue = billetes-totComp
    if billetes == totComp:
        print("Pago justo, muchas gracias, vuelva pronto")
    elif billetes > totComp:
        quin = vue//500
        vue = vue % 500
        cien = vue//100
        vue = vue % 100
        cincu = vue//50
        vue = vue % 50
        vein = vue//20
        vue = vue % 20
        diez = vue//10
        vue = vue % 10
        cinc = vue//5
        vue = vue % 5
        uno = vue//1
        print(quin, "billetes de 500", cien, "billetes de 100", cincu, "billetes de 50", vein,
              "billetes de 20", diez, "billetes de 10", cinc, "billetes de 5 y", uno, "billetes de 1")
    else:
        print("Falta dinero, intentelo nuevamente")


totComp = int(input("Ingrese el monto de la compra: "))
billetes = int(input("Ingrese el dinero recibido: "))
vuelto(totComp, billetes)
'''
# Ejercicio 4
'''
def patron1(x):
    for i in range (0, x):
        print ("*"*10)

def patron2(x):
    for i in range (0,x):
        print("*"*(2*i+2))
x=int(input("Ingrese un numero: "))
patron1(x)
patron2(x)
'''
# Ejercicio 5
'''
cuadrado =lambda x: x*x
num =int(input("Ingrese un numero: "))
print(cuadrado(num))
'''
#Ejercicio 6
'''
def parImp(x): return "par" if x % 2 == 0 else "impar"

#x = int(input("Ingrese un valor: "))
#print(parImp(x))

for i in range(0, 100):
    print(i,"es", parImp(i))
'''
#Ejercicio 7
'''
cuadrado =lambda x: x*x

x=int(input("Ingrese un numero: "))
original=[]
lista=[]
for i in range (1, (x+1)):
    original.append(i)
    lista.append(cuadrado(i)) 
print(lista[-10:len(lista)])
'''
#Ejercicio 8
'''
lista1=['In', 'the', 'list', 'comprehension', 'a', 'new', 'list', 'is', 'generated', ]
lista2=['list', 'It', 'is', 'also', 'possible' 'to', 'delete', 'items', 'using']
eliminada=[]
#Hago una copia nueva de la lista (Si uso solo = estoy creando una referencia a la lista original)
original=lista1.copy() 
for i in range (0, (len(original))):
    for x in range (0, (len(lista2))):
        if original[i]==lista2[x]:
            eliminada.append(original[i])
            lista1.remove(original[i])
print(original)
print(lista1)
print(eliminada)
'''
#Ejercicio 9
'''
def orden(lista):
    for i in range (0, (len(lista)-1)):

        if str(lista[i])<str(lista[i+1]):
            asc=True
        else:
            asc=False
    return (asc)

lista1=['In', 'the', 'list', 'comprehension', 'a', 'new', 'list', 'is', 'generated', ]
lista2=[1,2,3,4,5,6,7,8]
print(orden(lista1))
print(orden(lista2))
'''
#Ejercicio 10
'''
def capicua(cadena):
    f=len(cadena)-1
    for i in range (0, f):
        if cadena[i]==cadena[(f-i)]:
            capi=True
        else:
            capi=False
            break   
            # Importante, si la palabra es impar puede producirse un falso positivo, por eso es 
            # importante cortar el ciclo al encontrar un par de letras que no sean capicuas
    return(capi)

# Para testear usamos una lista sobre la cual iteramos
lista1=['In', 'the', 'list', 'comprehension', 'a', 'new', 'list', 'is', 'generated', 123]
def alReves(x):
      return x[::-1]

for i in range (0, len(lista1)):
    if i%2==0:
        cadena=str(lista1[i]+alReves(lista1[i])) #Quiero valores capicuas por lo que a las palabras en posiciones par, las espejo
        print(cadena," - ", capicua(cadena))
    else:
        cadena=str(lista1[i])
        print(cadena," - ", capicua(cadena))
'''
#Ejercicio 11
'''
cadena= input("Ingrese una frase: ")
largo=len(cadena)

if largo<80:
    blanco=(80-largo)//2 #me quedo con la parte entera de la division
    espa=" "*blanco
    if largo%2!=0: #agrego un " " mas al final para compensar frases con nº de caracteres impar
        extra=" "*1
    else:
        extra=" "*0
    print("-"+espa+cadena+espa+extra+"-") 
else:
    print("Su frase es demasiado larga")
'''
#Ejercicio 12
'''
def fechaExt(tupla):        #No tiene que devolver una tupla!!!!!
    meses=(" ", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    dia=tupla[0]
    if (int(tupla[1]))<1 or (int(tupla[1]))>12: # Garantizamos que el mes sea el correcto
        mes=("- Mes equivocado -")
    else: 
        mes=meses[int(tupla[1])]
    anio=tupla[2]
    if anio>21: 
        anio =1900+anio
    else:
        anio=2000+anio
    out=(str(dia)+" de "+ mes +" de "+str(anio))
    return (out)
    
fecha =(11, 8, 81)
print (fecha)
nFecha= fechaExt(fecha)
print (nFecha)
'''
# Clase usuario, no anda el getPass
'''
class usuario:
    def __init__(self, userName, password):
        self.userName=userName
        self.__password=password
    
    def setPass(self, password):
        self.__password=password

    def getPass(self):
        return(self.__password)
    
    def __str__(self):
        return (f"Usuario: {self.userName} Contraseña: {self.__password}")

pendejo = usuario("luis", "xxxx")
print(pendejo)
pendejo.setPass("1234")
pendejo.userName="Luis ALfonso Gomez"
print(pendejo.userName)
p=(pendejo.getPass()) #Me faltaban los () del metodo¿?
print(p)
print(pendejo)
'''
import math
class Punto:

    def __init__(self, x, y): #Constructor
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distOrigen (self):
        hipo=math.sqrt(self.x**2+self.y**2)
        return(hipo)
    
    def distDosP (self, p):
        distancia=math.sqrt((self.x-p.x)**2+(self.y-p.y)**2)
        return distancia
#Programa pricipal

p1 = Punto (3,1)
p2 = Punto (-1,-1)
print(p1)
print(p2)
print (f"la distancia al origen de {p1} es: {p1.distOrigen():.2f}")
print(p1.distDosP(p2))