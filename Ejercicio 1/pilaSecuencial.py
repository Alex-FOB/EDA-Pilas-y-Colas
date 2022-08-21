import numpy as np

class Pila:
    __tope = None
    __cant = None
    __arreglo = None
    def __init__(self, cant = 0):
        self.__cant = cant
        self.__tope = -1
        self.__arreglo = np.empty(self.__cantidad, dtype=int)
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
            return 0
        else:
            self.__tope-= 1
            x = self.__arreglo[self.__tope]
            np.delete(self.__arreglo, self.__tope) #añadido
            return x
    def mostrar(self):
        if(not self.vacia()):
            for i in range(self.__tope, 0):
                elemento = self.suprimir()
                if(elemento != 0):
                    print(elemento)