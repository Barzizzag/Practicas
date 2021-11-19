a = int(input("Ingrese el numero a: "))
b = int(input("Ingrese el numero b: "))
multiA=a
multiB=b
while (multiA!=multiB):
    print(multiA,multiB)
    if (multiA<multiB):
        multiA+=a    
    else:
        multiB+=b
print ("El multiplo de",a,"y",b,"es", multiB)