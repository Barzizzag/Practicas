import math
class  Punto:
    def __init__(self,x,y  ):
        self.x=x
        self.y=y

    def __str__(self):
        return f"({self.x},{self.y})"

    def distanciaAlOrigen(self):
        distancia=  math.sqrt(self.x**2 + self.y**2)
        return distancia
    def distanciaEntreDosPuntos(self, p):
        distancia=  math.sqrt((self.x-p.x)**2 + (self.y-p.y)**2)
        return distancia

class Rectangulo:
    #p1 es un objeto de la clase Punto 
    #p2 es un objeto de la clase Punto    
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

    def perimetro(self ):
        per=2* abs(self.p1.x-self.p2.x) + 2*abs(self.p1.y-self.p2.y)
        return per
    def superficie(self ):
        sup= abs(self.p1.x-self.p2.x) * abs(self.p1.y-self.p2.y)
        return sup


#programa principal
p1=Punto(4,1)
p2=Punto(1,4)
print(p1)
print(p2)
#print(f"Distancia al origen de punto {p1} es {p1.distanciaAlOrigen():.2f}")
#print(f"Distancia al origen de punto {p2} es {p2.distanciaAlOrigen():.2f}")
#print(f"Distancia entre el {p1}  y {p2} es {p1.distanciaEntreDosPuntos(p2):.2f}")
r=Rectangulo(p1,p2)
perimetro=r.perimetro()
print(f"Perimetro: {perimetro}")
sup=r.superficie()
print(f"Superficie: {sup}")