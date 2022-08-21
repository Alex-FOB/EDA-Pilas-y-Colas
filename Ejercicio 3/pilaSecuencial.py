import numpy as np

class Pila:
    __tope = None
    __cant = None
    __arreglo = None
    def __init__(self, cant = 0):
        self.__cant = cant
        self.__tope = -1
        self.__arreglo = np.empty(cant, dtype=int)
    def vacia(self):
        return self.__tope == -1
    def insertar(self, numero):
        if(self.__tope < self.__cant-1):
            self.__tope += 1
            self.__arreglo[self.__tope] = numero
            return numero
        else:
            return 0
    def suprimir(self):
        if(self.vacia()):
            print('Pila vacía')
            return -1
        else:
            x = self.__arreglo[self.__tope]
            self.__tope-= 1
            return x
    def mostrar(self):
        resultado = 1
        if(not self.vacia()):
            i = 0
            tope = self.__tope
            while i <= tope:
                elemento = self.suprimir()
                if(elemento != -1):
                    resultado *= elemento
                i += 1
        return resultado