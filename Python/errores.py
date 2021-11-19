'''
def cuad(n):
    	return n ** 2

n =int(input("Ingrese un número"))
print(n , " al cuadrado es " , cuad(n))
'''
def ingresarPositivo(msj):
    err=True
    while err:
        try:
            num=float(input(msj))
            if num>0:
                err=False
            else:
                print("Error: Debe ingresar un numero positivo")
        except:
            print("Error: ha ingresado un valor no numerico")
        #except:
        #    print("Error inesperado")
    return num


n=ingresarPositivo("Ingrese un numero mayor a cero")

def ingresarPositivo(msj):
    err=True
    while err:
        try:
            numReal=float(input(msj))
            num=int(numReal)
            assert(num==numReal)
            assert(num>0)
            break
        except AssertionError as error:
            print (error)
        except (ValueError):
            print("Error: ha ingresado un valor no numerico")
        except:
            print("Error inesperado")
    return num