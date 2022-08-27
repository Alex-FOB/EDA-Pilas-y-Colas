import numpy as np

class Pila:
    __tope1 = None
    __tope2 = None
    __cant = None
    __arreglo = None
    def __init__(self, cant = 0):
        self.__cant = cant
        self.__tope1 = -1
        self.__tope2 = cant
        self.__arreglo = np.empty(cant, dtype=int)
    #PILA 1----------------------------------------------
    def vacia1(self):
        return self.__tope1 == -1
    def insertar1(self, numero):
        if(self.__tope1 < self.__tope2-1):
            self.__tope1 += 1
            self.__arreglo[self.__tope1] = numero
            return numero
        else:
            return 0
    def suprimir1(self):
        if(self.vacia1()):
            print('Pila vacía')
            return -1
        else:
            x = self.__arreglo[self.__tope1]
            self.__tope1 -= 1
            return x
    def mostrar1(self):
        text = ''
        if(not self.vacia1()):
            i = 0
            tope = self.__tope1
            while i <= tope:
                elemento = self.suprimir1()
                if(elemento != -1):
                   text += '{}  '.format(elemento)
                i += 1
        return text
    #PILA 2----------------------------------------------
    def vacia2(self):
        return self.__tope2 == self.__cant+1
    def insertar2(self, numero):
        if(self.__tope2 > self.__tope1+1):
            self.__tope2 -= 1
            self.__arreglo[self.__tope2] = numero
            return numero
        else:
            return 0
    def suprimir2(self):
        if(self.vacia2()):
            print('Pila 2 - vacia')
            return -1
        else:
            x = self.__arreglo[self.__tope2]
            self.__tope2 += 1
            return x
    def mostrar2(self):
        text = ''
        if(not self.vacia2()):
            i = self.__cant - 1
            tope = self.__tope2
            while i >= tope:
                elemento = self.suprimir2()
                if(elemento != -1):
                    text += '{}  '.format(elemento)
                i -= 1
        return text 