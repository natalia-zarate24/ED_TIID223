#Clase que representa 
class Nodo:
    def __init__(self, numero):
        #Valor que tendra el nodo
        self.numero = numero

        #Apunta a nuestro siguiente nodo
        self.siguiente = None

#Clase que va a administrar a todos los nodos
class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None

    def Insertar_Nodo_al_Inicio(self, numero):
        nuevo_nodo = Nodo(numero)

        if(self.cabeza is None):

            self.cabeza = Nodo(numero)

            return
        
        nuevo_nodo.siguiente = self.cabeza

        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self,numero):
            
        nuevo_nodo = Nodo(numero)
        if(self.cabeza == None):

            self.cabeza = nuevo_nodo

            return

        #Referencia temporal
        actual=self.cabeza
        while(actual.siguiente):
            actual=actual.siguiente
            actual.siguiente=nuevo_nodo
            
    def imprimir_lista(self):
        actual=self.cabeza
        while(actual):
            print(actual.numero," -> ",end=" ")
            actual=actual.siguiente
        print("None")


mi_lista = ListasEnlazadas()
mi_lista.Insertar_Nodo_al_Inicio(5)
mi_lista.Insertar_Nodo_al_Inicio(4)
mi_lista.Insertar_Nodo_al_Inicio(3)
mi_lista.Insertar_Nodo_al_Inicio(2)
mi_lista.Insertar_Nodo_al_Inicio(1)

mi_lista.imprimir_lista()