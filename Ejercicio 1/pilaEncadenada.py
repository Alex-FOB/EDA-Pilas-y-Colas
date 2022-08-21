from nodo import Nodo

class Pila:
    __tope = None
    __cant = None
    def __init__(self, tope = Nodo(), cant = 0):
        self.__tope = tope
        self.__cant = cant
    def vacia(self):
        return self.__cant == 0
    def insertar(self, elemento):
        #ps1 = Nodo()
        ps1 = self.__tope
        ps1.setDato(elemento)
        ps1.setSiguiente(self.__tope)
        self.__tope = ps1
        self.__cant += 1
        return ps1.getDato()
    def suprimir(self):
        if(self.vacia()):
            print('Pila vacía')
            return 0
        else:
            aux = self.__tope
            x = self.__tope.getDato()
            self.__tope = self.__tope.getSiguiente()
            self.__cant -= 1
            del(aux)
            return x