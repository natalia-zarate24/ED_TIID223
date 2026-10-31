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
            self.cabeza = nuevo_nodo
            return

        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self,numero):
        nuevo_nodo = Nodo(numero)
        if(self.cabeza == None):
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_nodo_al_inicio(self):
        if self.cabeza is not None:
            self.cabeza = self.cabeza.siguiente

    def eliminar_nodo_al_final(self):
        if self.cabeza is None:
            return

        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente
        actual.siguiente = None
            
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

print("Lista original:")
mi_lista.imprimir_lista()

mi_lista.eliminar_nodo_al_inicio()
mi_lista.eliminar_nodo_al_final()

print("lista después de eliminar el inicio y el final: ")
mi_lista.imprimir_lista()