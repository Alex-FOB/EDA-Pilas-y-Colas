class Celda:
    __dato = None
    __siguiente = None
    def __init__(self, dato = None):
        self.__dato = dato
        self.__siguiente = None
    def loadSiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getSiguiente(self):
        return self.__siguiente
    def loadDato(self, dato): #no es necesario
        self.__dato = dato
    def getDato(self):
        return self.__dato