#Ejercicio 1
"""
vector = []
for n in range(5):
    nuevo = float(input("Ingrese el siguiente número:"))
    vector.append(nuevo)
menor = vector[0] #Se cambio por un elemento del vector (El cero puede no estar en el vector y ser el menor)
for elemento in vector:
    if elemento < menor:
        menor = elemento
print("El número menor es:", menor)
"""
#Ejercicio 2
"""
vector= [1, 5, 3, 9, 10, 8]
mayor=vector[0]
for i in range (len(vector)):
   if vector[i]>mayor:
       mayor=vector[i]
print("El mayor es:",mayor)
"""
#Ejercicio 3
"""
vector= [5, 9, 15, 2, -8, 3]
mayor=vector[0]
menor=vector[0]
for i in range (len(vector)):
    if vector[i]>mayor:
        mayor=vector[i]
    if vector[i]<menor:
        menor=vector[i]
print("El mayor es:",mayor)
print("El menor e:",menor)
"""
#Ejercicio4
"""
vector= [-5, -9, -15, -2, -8, -3]
mayor=vector[0]
menor=vector[0]
for i in range (len(vector)):
    if vector[i]>mayor:
        mayor=vector[i]
    if vector[i]<menor:
        menor=vector[i]
print("El mayor es:",mayor)
print("El menor e:",menor)
"""
#Ejercicio 5
"""
vector=[8, 10, 15, 2, 8, 6, 21, 5]
mayor1=vector[0]
mayor2=vector[0]
for i in range (len(vector)):
    if vector[i]>mayor1:
        mayor2=mayor1
        mayor1=vector[i]
    elif vector[i]>mayor2:
        mayor2=vector[i]
print("El primer mayor es:",mayor1,"el segundo mayor es:",mayor2)
"""
#Ejercicio 6
"""
vector1=[5,-2, 8, 10, -4, 13, 21]
vector2=[]
for i in range (len(vector1)):
    numero=vector1[i]
    vector2.append(numero+2)
print(vector2)
"""
#Ejercicio 7
"""
def Mayor(vector):
    vector=vector
    mayor=vector[0]
    for i in range (len(vector)):
        if vector[i]>mayor:
            mayor=vector[i]
    return mayor
def Menor(vector):
    vector=vector
    menor=vector[0]
    for i in range (len(vector)):
        if vector[i]<menor:
            menor=vector[i]
    return menor
vector=[]
for i in range(10):
    entrada=float(input("Ingrese un numero: "))
    vector.append(entrada)
print ("El mayor es:", Mayor(vector),";el menor es:", Menor(vector))
"""
#Otra forma
"""
vector=[]
for i in range(10):
    entrada=float(input("Ingrese un numero: "))
    vector.append(entrada)
menor=vector[0]
mayor=vector[0]
for i in range(10):
    if vector[i]<menor:
        menor=vector[i]
    if vector[i]>mayor:
        mayor=vector[i]
print("El mayor es:",mayor,",el menor es:",menor)
"""
#Ejercicio 8
"""
vector=[]
for i in range (10):
    vector.append(float(input("Ingrese un numero:")))   #Solo para ver si lo hace
promedio=0
for numero in vector:
    promedio=promedio+numero
print("El promedio es: ",promedio)
"""
#Ejercicio 9
"""
vector=[]
bandera=True

while bandera:
    entrada=float(input("Ingrese un numero: "))
    if entrada!=0:
        vector.append(entrada)
    else:
        bandera=False

minimo=vector[0]
maximo=vector[0]
promedio=0

for numero in vector:
    promedio=promedio+numero
for i in range (len(vector)):
    if vector[i]<minimo:
        minimo=vector[i]
    if vector[i]>maximo:
        maximo=vector[i]

print("El minimo es:",minimo,"el maximo es:",maximo,"y el promedio es:",promedio)
"""
#Ejercicio 10

vector=[]
bandera=True
while bandera:
    ingreso=float(input("Ingrese un numero: "))
    if ingreso>=0:
        vector.append(ingreso)
    else:
        bandera=False
for  i in range (len(vector)-1):
    diferencia=vector[i]-vector[i+1]
    print("La diferencia entre el elemento",i,"y el",(i+1),"es:",diferencia)