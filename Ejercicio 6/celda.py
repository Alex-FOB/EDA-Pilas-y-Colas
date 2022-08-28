class Celda:
    __dato = None
    __siguiente = None
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    def loadSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__dato