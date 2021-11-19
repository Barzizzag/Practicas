#Ciclo For
"""
    Es el ciclo clasico que se usa para repetir una tarea n cantidad de veces 
    siendo n un numero sabido de antemano.
    El pro es que es facil de pensar, sabemos cuantas veces se repite la tarea y ya fue.
"""
suma=0
for i in range (10):
    numero = int(input("Ingrese un numero: "))
    suma=suma + numero
    #funciona tambien 
    #suma+=numero
print("La suma es:",suma)

#Ciclo While
""" 
    Es el otro ciclo clasico en el cual algo se repite hasta que las condicion sea falsa. luego sale
"""
suma2=0
n=0 #Esta variable existe solo para contar cuantas veces se sumo en esta demostracion.
i=int(input("Ingrese cuantos numeros quiere sumar: ")) #Tengo la opcion de ingresar cero y no se ingresa al ciclo
while (i>0):
    numero=int(input("Ingrese otro numero: "))
    suma2+=numero
    n=n+1
    i-=1
print("La nueva suma es:", suma2, "cantidad de veces que corrio el ciclo:",n,"veces")

#Ciclo do-while
"""
    Como el do-while clasico no existe, tenemos que hacer trampa y forzar el ciclo.
    Con una "bandera" o condicion o como quieran llamarlo.
"""
finCiclo=False
suma3=0
n=0
while (finCiclo==False):
    numero=int(input("Ingrese otro numero (Sí, de nuevo): "))
    suma3=suma3+numero
    n+=1    #Nuevamente cuento los ciclos para la demostracion. 
    continuar=input("Ingrese NO para continuar: ")
    if (continuar.upper()=="NO"):
        finCiclo=True
print("La suma del DO-WHILE es:",suma3, "se repitio el ciclo:",n,"veces")