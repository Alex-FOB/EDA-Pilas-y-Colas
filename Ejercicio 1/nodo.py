class Nodo:
    __dato = None
    __siguiente = None
    def __init__(self):
        self.__dato = None
        self.__siguiente = Nodo()
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente
    def setDato(self, dato):
        self.__dato = dato
    def getDato(self):
        return self.__dato