from celda import Celda

class cola:
    __cant = None
    __primer = None 
    __ultimo = None
    def __init__(self, cant = 0, primer = None, ultimo = None):
        self.__cant = cant
        self.__primer = primer
        self.__ultimo = ultimo
    def vacia(self):
        return self.__cant == 0
    def insertar(self, dato):
        aux = Celda(dato)
        aux.loadSiguiente(None)
        if(self.__ultimo == None):
            self.__primer = aux
        else:
            self.__ultimo.loadSiguiente(aux)
            self.__ultimo = aux
            self.__cant += 1
        return self.__ultimo.getDato()
    def suprimir(self):
        if(self.vacia()):
            print('Cola vacia')
            return -1
        else:
            aux = self.__primer
            x = self.__primer.getDato()
            self.__primer = self.__primer.getSiguiente()
            self.__cant -= 1
            if(self.__primer == None):
                self.__ultimo = None
            del(aux)
            return x
    def getPrimer(self):
        return self.__primer
    #def recorrer(self):