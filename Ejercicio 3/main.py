from cmath import exp
import imp
from pilaSecuencial import Pila

def factorial(numero):
    pila = Pila(numero)
    for i in range(numero):
        pila.insertar(numero - i)
    return pila
if __name__ == '__main__':
    numero = int(input('Ingrese un numero: '))
    resultado = factorial(numero)
    print('Factorial: ', resultado.mostrar())
    input()