#Ejercicio 1
for i in range (10):
    multiplicacion = i*4
    print (i,"* 4 =",multiplicacion)

#Ejercicio 2
suma=0
while suma<10:
    nuevo=int(input("Ingrese un nuevo número: "))
    suma=suma+nuevo
print ("La suma es: ", suma)

#Ejercicio 3
i=0
while i<10:
    print(i+1)
    i+=1

#Ejercicio 4
i=11
while i>1:
    print(i-1)
    i-=1

#Ejercicio 6
i=1
        # range ([2]inicio, [1]fin, [3]paso)
for i in range (1, 12, 2):
    print (i," | ",i+1)
for i in range (1, 7):
    print (i, "\t", i+6)

#Ejercicio 7

ingreso=1
sumar=0
while ingreso!=0:
    ingreso=(int(input("Ingrese un número: ")))
    sumar=sumar+ingreso
print("La suma es: ",sumar)

#Ejercicio 8
ingreso=1
sumando=0
contador=0
while ingreso!=0:
    ingreso=int(input("Ingrese un número (sí, otra vez): "))
    sumando=sumando+ingreso
    contador+=1
promedio=sumando/(contador-1)
print (sumando, contador, promedio)

#Ejercicio 9
ingreso=0
acumulado=0
prome=0
contador=0
while acumulado<20:
    ingreso=int(input("Ingrese más números: "))
    acumulado+=ingreso
    contador+=1
prome=acumulado/(contador)
print (acumulado,contador,prome)
