class Madre:
    def __init__(self):
        print("Soy Madre")

class Padre:
    def __init__(self):
        print("Soy Padre")       

class Hijo(Madre, Padre):#Opcion 3: cuando se tiene dos Super clases se toma primero el de la izquierda
    #pass #Opcion 1: se usa para cuando se tiene una sola super clase qu quiere heredar todo de la super clase
    def __init__(self):
        #super().__init__() #Opcion 2: en este caso no se usa self ya que lo llva implicito super.
        Padre.__init__(self)#Opcion 3:para que tome al padre se puede escribir de esta manera y se agrag (self)
        Madre.__init__(self)
        print("Soy Hijo")

hijo=Hijo()##instancia