#Ejercicio 1
edad=int(input("Ingrese su edad:"))
if (edad>16): #Cambio de signo 
    print("La edad es:",edad)

#Ejercicio 2
        #No tengo idea del error? Sera el float?
dado1=float(input("Ingrese el valor del 1er dado:"))
dado2=float(input("Ingrese el valor del 2do dado:"))
suma= dado2+dado1
if (suma >7):
    print("La suma es mayor a 7")
else:
    print("La suma es menor a 7")

#Ejercicio 3
edad=int(input("Ingrese su edad: "))
if (edad<18):
    print("Debe ser mayor de edad")

#Ejercicio 4
edad=int(input("Ingrese su edad: "))
if (edad<18):
    print("Debe ser mayor de edad")
else:
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")

#Ejercicio 5
edad=int(input("Ingrese su edad:"))
if (edad<16):
    print ("Debe ser mayor de 16")
elif (edad<18):
    nombre =input("Ingrese su nombre: ")
    tutor =input("Ingrese el nombre de un adulto responsable: ")
else:
    nombre = input ("Ingrese su nombre: ")

#Ejercicio 6
nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
if (edad>16):
    print("Bienvenido",nombre)
else:
    print("Deberia ser mayor de 16")

#Ejercicio 7
acumulado=0
for i in range(3):
    numero=float(input("Ingrese una nota: "))
    acumulado=acumulado+numero
promedio=acumulado/3
if (promedio<4):
    print("Esta desaprobado")
elif (promedio<7):
    print("Debe rendir final")
else:
    print ("Promociona con ",promedio)