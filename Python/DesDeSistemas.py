#Ejercicio 1
"""
bandera=True
while bandera:
    print("Opciones: \n 1-Nuevo \n 2-Editar \n 3-Borrar \n 4-Salir")
    entrada=input("Ingrese una opcion: ")
    if entrada=="1":
        print("El ingreso es: Nuevo")
        bandera=False
    elif entrada=="2":
        print("El ingreso es: Editar")
        bandera=False
    elif entrada=="3":
        print("El ingreso es: Borrar")
        bandera=False
    elif entrada=="4":
        print("El ingreso es: Salir")
        bandera=False

#Ejercicio 2

def menu():
    print("Opciones: \n 1-Nuevo \n 2-Editar \n 3-Borrar \n 4-Salir")
    entrada=input("Ingrese una opcion: ")
    if entrada=="1":
        print("El ingreso es: Nuevo")
    elif entrada=="2":
        print("El ingreso es: Editar")
    elif entrada=="3":
        print("El ingreso es: Borrar")
    elif entrada=="4":
        print("El ingreso es: Salir")
    if int(entrada) <=4:    
        return False
    else:
        return True
while menu():
    print("Opcion invalida")

#Ejercicio 3

def menu(diccionario): 
    print("Opciones: \n N-Nuevo \n E-Editar \n B-Borrar \n S-Salir")
    key=input("Ingrese una opcion: ").upper()
    return key 

menu_principal={"N":"Nuevo", "E":"Editar", "B":"Borrar", "S":"Salir"} 

opción=menu(menu_principal) 
print("Opción seleccionada:",menu_principal[opción])

#Ejercicio 4

def salidaEnTupla():
    nombreEmpresa=input("Ingrese el nombre de la empresa: ")
    nombreContacto=input("Ingrese el nombre del contacto: ")
    email=input("Ingrese el email:")
    return (nombreEmpresa, nombreContacto, email)

print(salidaEnTupla())
"""
#Ejercicio 5
def bisiesto(fechaEnLista):
    dia=int(fechaEnLista[0])
    mes=int(fechaEnLista[1])
    anio=int(fechaEnLista[2])
    bisiesto=False
    if ((anio%4==0) and ((anio%100!=0)or(anio%400==0))):
        bisiesto=True
    mesLargo=False
    if anio<0:
        print("No puede ingresar un año negativo")
        return False
    else:
        if (mes<1 or mes>12):
            print("El mes ingresado no es valido")
            return False
        else:
            if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
                mesLargo=True
            if dia<1:
                print("Un dia no puede ser negativo")
                return False
            elif dia>31:
                print("No hay mas de 31 dias en un mes")
                return False
            elif (mes==2 and dia>28 and bisiesto==False):
                print ("Fecha invalida no es año bisiesto y febrero no puede tener mas de 28 dias")
                return False
            elif (mes==2 and dia>29 and bisiesto==True):
                print ("Fecha invalida a pesar de ser año bisiesto, febrero no puede tener mas de 29 dias")
                return False
            elif (dia>30 and mesLargo==False):
                print("Fecha invalida el mes",mes," no puede tener mas de 30 dias")
                return False
            else:
                return True

def fechas(fechaEnLista):   #texto.split - ISO8601 aaaa-mm-dd
    dia=fechaEnLista[0]
    if len(dia)==1:
        dia="0"+dia
    mes=fechaEnLista[1]
    if len(mes)==1:
        mes="0"+mes
    anio=fechaEnLista[2]
    if len(anio)==2:
        if int(anio)>21:
            anio="19"+anio #Vamos a suponer que nadie va a introducir un año anterior a 1922
        else:
            anio="20"+anio
    fecha= anio+"-"+mes+"-"+dia
    return fecha

fecha=input("Ingrese una fecha")
fechaEnLista=fecha.split("/")
if len(fechaEnLista)==1:
    fechaEnLista=fecha.split("-")

if bisiesto(fechaEnLista):
    print(fechas(fechaEnLista))

"""
#Ejercicio 6


product=["Samsung", "LA5890",12345,128]
def producto(product):
    print ("Marca:",product[0],"\nmodelo:",product[1],"\nprecio:",product[2],"\ncantidad en stock:",product[3])
producto(product)

#Ejercicio 7

lista=[("Samsung", "LA5890",12345,28),("Samsung", "LB001",2550,205),("LG", "GL-2552",25400,18)]
def producto(lista):
    marca="Marca"
    modelo="Modelo"
    precio="Precio"
    stock="Stock"
    fill=" "
    align="^"
    width=14
    print("|",f'{marca:{fill}{align}{width}}',"|",
            f'{modelo:{fill}{align}{width}}',"|",
            f'{precio:{fill}{align}{width}}',"|",
            f'{stock:{fill}{align}{width}}',"|")
    print("-"*69)
    for i in range(len(lista)):
        marca=lista[i][0]
        modelo=lista[i][1]
        precio=lista[i][2]
        stock=lista[i][3]
        print("|",f'{marca:{fill}{align}{width}}',"|",
            f'{modelo:{fill}{align}{width}}',"|",
            f'{precio:{fill}{align}{width}}',"|",
            f'{stock:{fill}{align}{width}}',"|")
        

producto(lista)
"""