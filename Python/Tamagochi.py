class Tamagotchi:
    nombre = ""
    hambre = 0
    animo = 0
    energia = 0

    def __init__(self, nombre, hambre, animo, energia):
        self.nombre = nombre
        self.hambre = hambre
        self.animo = animo
        self.energia = energia

    def jugar(self):
        self.animo += 2
        self.energia -= 1
        print("Estoy Jugando")

    def alimentar(self):
        self.animo += 1
        self.hambre += 3
        print("Me estoy Alimentando ")

    def dormir(self):
        self.hambre -= 1
        self.energia += 3
        print("Estoy Durmiendo")


    def pasar(self):
        self.animo -= 1
        self.hambre -= 1
        self.energia -= 1
        print("Esta pasando el tiempo")

    def __str__(self):
        return (f"Nombre:{self.nombre} Animo:{self.animo} Hambre:{self.hambre}  Energia:{self.energia} ") 


# Programa Principal
muerto=False
ciclo=0
t = Tamagotchi("", 10, 10, 10)
t.nombre=input("Ingrese el nombre: ")
while muerto!=True:
    print(t)
    ciclo=ciclo+1
    acc=input("Ingrese accion (dormir, comer o jugar): ")
    if acc=="dormir":
        t.dormir()
    elif acc=="comer":
        t.alimentar()
    elif acc=="jugar":
        t.jugar()
    else:
        print("Comando no reconocido")
        ciclo-=1
    if acc=="muere": #para cancelar el ciclo antes de tiempo
        muerto=True
    t.pasar()
    if t.hambre<=0:
        muerto=True
    if t.animo<=0:
        muerto=True
    if t.energia<=0:
        for cont in range(1, 5):
            t.dormir()

print(t.nombre," vivio ",ciclo," ciclos")