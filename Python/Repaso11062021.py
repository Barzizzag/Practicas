#todo numero entero es divisible por 1 y por si mismo
#los divisores de 7 son: 1 y 7
#los divisores de 11 son : 1 y 11
#los divisores de 30 son: 1  2  3  5  6  10 15  30

#Un numero primo es un nro entero que solo es divisible por 1 y por si mismo
# 6 : 1  2  3  6    el 6 no es primo
# 3 : 1  3          el 3 es primo
#17 : 1  17         el 17 es primo


#7) Escribe un programa que pida un número y diga si es divisible por 2
'''
n=int(input("ingrese un nro entero: ")
if   n%2==0 :
    print("El", n ,"ingresado es divisible por 2")
else:
    print("El nro ingresado es divisible por 2")
'''


#8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7
#    (sólo hay que comprobar si lo es por uno de los cuatro)
#Ej: si ingresa un 2 dira por pantalla es divisible por 2 o 3 o 5 o 7

'''
n=int(input("ingrese un nro entero: ")
if n%2==0 or n%3==0 or n%5==0 or n%7==0  :
    print("El nro ingresado es divisible por 2 o 3 o 5 o 7")
'''

#9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay
#que decir todos por los que es divisible)
#Ej 210: 2, 3, 5, 7''' 

'''
n=int(input("ingrese un nro entero: ")
if n%2==0   :
    print("El nro ingresado es divisible por 2 ")
if n%3==0 :
    print("El nro ingresado es divisible por 3 ")
if n%5==0 :
    print("El nro ingresado es divisible por 5 ")
if n%7==0 :
    print("El nro ingresado es divisible por 7 ")
'''
#10) Escribir un programa que escriba en pantalla los divisores de un número dado
# los divisores de 60 son:   1  2  3  5 y 6
# repasemos range(m,n,p)  comienza en m, va a repetir  hasta n-1 , va a incrementar con paso p
'''
n=int(input("ingrese un nro entero: ")
for  i in range(1,n+1,1) :
    if n%i==0:
        print(f"El nro {n} es divisible por {i}")
'''
#11) Escribir un programa que nos diga si un número dado es primo (no es divisible
#por ninguno otro número que no sea él mismo o la unidad)
#Definicion: un nro es primo cuando solo es divisible por 1 y pos si mismo
# los divisores de 6: 1 2 3 6 
# los divisores de 11111166969 : 

n=int(input("ingrese un nro entero: "))
i=2 
while i < n  and  n%i != 0   :    # mientras i no llegue al final Y  i no es divible por n                                        
    i=i+1                         # true AND  true= true
if i < n :
    print(f"El numero {n} No es primo")
else:
    print(f"El numero {n} es primo")
# Valores que van tomando las variables i , n y lo que va mostrando por pantalla
#| i |  n  |  muestra por pantalla
#|-------------------------------
#| 2 |  7  |  
#| 3 |  7  | 
#| 4 |  7  |
#| 5 |  7  |
#| 6 |  7  |
#| 7 |  7  |   El numero 7 es primo


#13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente
#    forma:
# 1
# 22
# 333
# 4444
# 55555
# 666666


'''
for i in range(1,31,1):
    renglon=""
    for j in range(1,i+1,1):
        renglon=renglon+ str(i)
    
    print(renglon)
'''

# otra forma de  hacerlo con el operador "*" entre string que se ve en la clase 21
# ejemplo   "cad"*2    "cadcad"
# "3"*3      "333"

for i in range(1,31,1):
       print( str(i)*i)       # repite i veces str(i)


# tabla del contenido de la variables i, j y lo que muestra por pantalla en cada paso del programa 
#| i  |  j   | renglon       | muestra por pantalla i  |
#------------------------------------------------------|
#| 1  |   1  |    ""+"1"     |     "1"                 |
#| 2  |   1  |    ""+"2"     |                         | 
#| 2  |   2  |    "2"+"2"    |      "22"               |
#| 3  |   1  |    ""+"3"     |                         |
#| 3  |   2  |    "3"+"3"    |                         |
#| 3  |   3  |    "33"+"3"   |      "333"              | 
#| 4  |   1  |    ""+"4"     |                         |
#| 4  |   2  |    "4"+"4"    |                         |
#| 4  |   3  |    "44"+"4"   |                         |
#| 4  |   4  |    "444"+"4"  |      "4444"             |
