#Ejercicio 1
"""
def promedio(valor1, valor2): 
    ''' Función promedio: Calcula el promedio de 2 números. 
    Entrada: valor1, valor2 
    Salida: Promedio (float) '''
    promedio = (valor1 + valor2)/2.0
    return promedio
#Programa principal 
n1 = float(input("Ingrese el valor 1:"))
n2 = float(input("Ingrese el valor 2:"))
prom = promedio(n1,n2) 
print("Promedio:",prom)
"""
#Ejercicio 2
"""
def es_triangulo (A, B, C):
    ''' Función es_triángulo: Verifica si se puede formar un triángulo, 
    dados las medidas de 3 segmentos. 
    Si la suma de 2 lados en menor que el tercero, 
    no se puede hacer un triángulo ''' 
    if (A+B)>C: 
        return True 
    elif (A+C)>B: 
        return True 
    elif (B+C)>A: 
        return True 
    else:
        return False 
#Programa principal
L1 = float(input("Ingrese la longitud del 1er lado:")) 
L2 = float(input("Ingrese la longitud del 2do lado:")) 
L3 = float(input("Ingrese la longitud del 3er lado:")) 
if es_triangulo(L1,L2,L3): 
    print("Se puede formar un triángulo") 
else:
    print("No se puede formar un triángulo")
"""
#Ejercicio 3
"""
def par(ingreso):
    numero=ingreso%2
    return numero
    
ingreso=int(input("Ingrese un numero: "))
numero=par(ingreso)
if (numero==0):
    print("Es par")
else:
    print("Es impar")
"""
#Ejercicio 4
"""
def mayor(num1,num2):
    if (num1>num2):
        aux=num1
    else:
        aux=num2
    return aux

numero1= float(input("Ingrese el primer numero: "))
numero2= float(input("Ingrese el segundo numero: "))
numeroMayor=mayor(numero1, numero2)
print("El mayor es:",numeroMayor)
"""
#Ejercicio 5
"""
def menor(num1, num2, num3):
    if num1==num2==num3:
        print("Los numeros son iguales")
        mini=0
    else:
        if num1<num2:
            if num1<num3:
                mini=num1
            else:
                mini=num3
        else:
            if num2<num3:
                mini=num2
            else:
                mini=num3
    return mini

numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
numero3=float(input("Ingrese el tercer numero: "))
minimo=menor(numero1, numero2, numero3)
print (minimo)
"""
#Ejercicio 6
"""
def promedio(num1,num2,num3):
    prom=(num1+num2+num3)/3
    return prom

numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
numero3=float(input("Ingrese el tercer numero: "))
prome=promedio(numero1, numero2, numero3)
print("El promedio es:",prome)
"""
#Ejercicio 7
"""
def primo(numero,ciclo):
    if (numero%ciclo==0):
        seraPrimo=False
    else:
        seraPrimo=True   
    return seraPrimo

bandera=True
num=int(input("Ingrese un entero: "))
ciclo=2
while bandera:
    esPrimo=primo(num,ciclo)
    '''En el primer ciclo compruebo si es multiplo de 2 y sumo 1, 
    luego no vuelvo a probar con los numeros pares ya que son todos 
    multiplos de dos'''
    if ciclo==2:
        ciclo+=1
    else:
        ciclo+=2
    if (num>=ciclo)or (esPrimo==False):
        bandera=False
print("¿El numero",num,"es primo?",esPrimo)
"""
#Ejercicio 8
"""
import random
def dados(cantidad):
    total=0
    for i in range (cantidad):
        dado=random.randint(1,6)
        # print ("Dado",(i+1),"salio",dado)
        total=total+dado
    return total

cantidad= int(input("Ingrese la cantidad de dados a lanzar: "))
print("El total de los dados lanzados es",dados(cantidad))
"""