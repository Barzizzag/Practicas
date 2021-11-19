#Ejercicio 1
fechaEnLista= ["12","12","12"]
#dia=int(input("Ingrese el dia: "))
#mes=int(input("Ingrese el mes: "))
#anio=int(input("Ingrese el año: "))
dia=int(fechaEnLista[0])
mes=int(fechaEnLista[1])
anio=int(fechaEnLista[2])
bisiesto=False
if ((anio%4==0) and ((anio%100!=0)or(anio%400==0))):
   bisiesto=True
mesLargo=False
valido=False
if anio<0:
    #print("No puede ingresar un año negativo")
    print("Fecha invalida")
else:
    if (mes<1 or mes>12):
        #print("El mes ingresado no es valido")
        print("Fecha invalida")
    else:
        if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
            mesLargo=True
        if dia<1:
            #print("Un dia no puede ser negativo")
            print("Fecha invalida")
        elif dia>31:
            #print("No hay mas de 31 dias en un mes")
            print("Fecha invalida")
        elif (mes==2 and dia>28 and bisiesto==False):
                print ("Fecha invalida")
        elif (mes==2 and dia>29 and bisiesto==True):
            print ("Fecha invalida")
        elif (dia>30 and mesLargo==False):
            print("Fecha invalida")
        elif (dia>31 and mesLargo==False):
            print("Fecha invalida")
        else:
            print("Fecha valida")

#Ejercicio 2
'''
for i in range (6,-1,-1):
    for j in range (i,-1,-1):
        print (i,"|",j)
'''
#Ejercicio 3
'''
segundos=int(input("Ingrese el tiempo en segundos: "))
hora=segundos//3600
resto=segundos%3600
minuto=resto//60
resto=segundos%60
print('{:0>2}'.format(hora),":",'{:0>2}'.format(minuto),":", '{:0>2}'.format(resto))
'''
#Ejercicio 4
'''
#PARAMETRO INGRESADO EN EL PROGRAMA (NO LO PEDIMOS; YA EXISTE)
pesoPaquete=500;
peso=0;
#BANDERA PARA EL CICLO WHILE
continuar=True
while continuar:
    #ESTO PODRIA SER UN FLOAT SI QUEREMOS INGRESAR PESOS NO EXACTOS
    ingreso=int(input("Ingrese el peso en gramos: "))
    peso=peso+ingreso
    #ACA CONTROLAMOS EL PESO DEL PAQUETE Y EN CASO DE QUE YA ESTE LLENO HACEMOS EL CAMBIO DE PAQUETE Y PREGUNTAMOS SI DESEA CONTINUAR
    if peso>=pesoPaquete:
        peso=0
        print("Debe cambiar el paquete")
        salida=input("¿Desea continuar? Ingrese NO para terminar: ")
        if salida=="NO":
            continuar=False
'''

#Ejercicio 5
'''
capacidadCilo=1000
suficiente=True
while suficiente:
    cantidadRequerida=float(input("Ingrese la cantidad de harina expresada en kilos: "))
    if capacidadCilo>=cantidadRequerida:
        print("Hay harina suficiente")
        print("Quedan",capacidadCilo-cantidadRequerida)
        capacidadCilo-=cantidadRequerida
    else:
        print("La cantidad de harina disponible no alcanza")
        print("Faltan",cantidadRequerida-capacidadCilo,"kilos de harina")
        suficiente=False
'''