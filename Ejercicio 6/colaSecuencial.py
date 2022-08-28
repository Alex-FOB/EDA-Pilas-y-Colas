import numpy as np

class cola:
    __arreglo = None
    __max = None
    __primer = None
    __ultimo = None
    __cant = None
    def __init__(self, max = 0):
        self.__arreglo = np.empty(max, dtype=int)
        self.__max = max
        self.__primer = 0
        self.__ultimo = 0
        self.__cant = 0
    def vacia(self):
        return self.__cant == 0
    def insertar(self, dato):
        if(self.__cant < self.__max):
            self.__arreglo[self.__ultimo] = dato
            self.__ultimo = (self.__ultimo+1) % self.__max
            self.__cant += 1
            return dato
        else:
            return 0
    def suprimir(self):
        if(self.vacia()):
            print('Pila vacía')
            return -1
        else:
            x = self.__arreglo[self.__primer]
            self.__primer = (self.__primer+1) % self.__max
            self.__cant -= 1
            return x
    def recorrer(self): #revisar
        if(not self.vacia()):
            i = self.__primer
            j = 0
            while j < self.__cant:
                i = (i+1) % self.__max
                self.__arreglo[i]
                j += 1