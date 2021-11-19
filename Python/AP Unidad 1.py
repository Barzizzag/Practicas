# Ejercicio 1
'''
print("Hola mundo")
'''
# Ejercicio 2
'''
print(3+5)
'''
# Idem con variables
'''
num1=3
num2=5
resu=num1+num2
print("El resultado es", resu)
'''
# Ejercicio 3
'''
nom=input("Ingrese su nombre:")
print("Hola", nom)
'''
#Ejercicio 4
'''
num1=input("Ingrese el primer numero") #El ingreso es "STRING"
num2=input("Ingrese el segundo numero")
resu=float(num1)+float(num2)# Los paso a FLOAT (o int para enteros)
print("El resultado es", resu)
'''
#Ejercicio 5
'''
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
if num1>num2:
    print("El primer numero es el mayor")
else:
    print("El segundo numero es el mayor")

# Otro modelo, la condicion VoF hace que se muestre la primera parte del mensaje o la segunda
print("el primero es mayor"*(num1>num2)+"el segundo es mayor"*(num2>num1))
'''
# Ejercicio 6
'''
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
if num1>num2:
    if num1>num3:
        print("El numero", num1,"es el mayor")
    else:
        print("El numero", num3,"es el mayor")
else:
    if num2>num3:
        print("El numero", num2,"es el mayor")
    else:
        print("El numero", num3,"es el mayor")
'''
#Ejercicio 7
'''
num1=float(input("Ingrese un numero: "))
resto=num1%2
if resto==0:
    print("El numero",num1,"es par")
else:
    print("El numero",num1,"no es par")
'''
#Ejercicio 8/9
'''
num=int(input("Ingrese el numero:"))
res2=num%2
res3=num%3
res5=num%5
res7=num%7
if res2==0:
    print(num, "Es divisible por 2")
elif res3==0:
    print(num, "Es divisible por 3")
elif res5==0:
    print(num, "es divisible por 5")
elif res7==0:
    print(num, "es divisible por 7")
'''
#Ejercicio 10
'''
num=int(input("Ingrese el numero:"))
for i in range(1,num+1,1):
    if num%i==0:
        print(f'{num} es divisible por {i}')
'''
#Ejercicio 11
'''
num=int(input("Ingrese el numero:"))
primo=True
i=2


while i!=(num): #Usar una bandera distinta para salir
    if num%i==0:
        primo=False
    print(i, primo)
    i+=1
    
if primo==True:
    print(f'{num} es primo')
else:
    print(f'{num} no es primo')
'''
#ejercicio 12
'''
num=int(input("Ingrese la calificacion:"))
if (num>=0 and num<3):
    print("Calificacion muy deficiente")
elif (num>=3 and num<5):
    print("Calificacion insuficiente")
elif (num>=5 and num<6):
    print("Calificacion suficiente")
elif (num>=6 and num<7):
    print("Calificacion bien")
elif (num>=7 and num<9):
    print("Calificacion notable")
elif (num>=9 and num<10):
    print("Calificacion sobresaliente")
else:
    print("Error en la calificacion")
'''
#Ejercicio 13
'''
num=int(input("Ingrese un numero: "))
y=0
for i in range (1, num+1):
    y+=1
    print(str(i)*y)
'''
#Ejercicio 14
'''
num=int(input("Ingrese un numero: "))
y=num
while num>0:
    print (str(num)*num)
    num-=1
'''
#Ejercicio 15
num=1
while num<=500:
    
    if (num%4==0)and(num%9==0)and(num%5==0):
        print (num, "es multiplo de 4 y de 9")
        print ("-"*20)
    elif (num%4==0)and(num%9!=0)and(num%5==0):
        print (num, "es multiplo de 4")
        print ("-"*20)
    elif (num%4!=0)and(num%9==0)and(num%5==0):
        print (num, "es multiplo de 9")
        print ("-"*20)
    elif (num%4!=0)and(num%9!=0)and(num%5==0):
        print (num)
        print ("-"*20)
    elif (num%4!=0)and(num%9==0)and(num%5!=0):
        print (num, "es multiplo de 9")
    elif (num%4==0)and(num%9!=0)and(num%5!=0):
        print (num, "es multiplo de 4")
    else:
        print (num)
    num+=1