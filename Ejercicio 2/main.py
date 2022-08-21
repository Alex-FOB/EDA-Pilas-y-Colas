from pilaSecuencial import Pila

def divisionesSucesivas(numero):
    pila = Pila(8)
    band = False
    while not band:
        resto = numero % 2
        numero = numero // 2
        if(numero == 0 or numero == 1):
            pila.insertar(resto)
            pila.insertar(numero)
            band = True
        else:
            pila.insertar(resto)
    return pila
if __name__ == '__main__':
    numero = int(input('Ingrese un numero entero: '))
    resultado = divisionesSucesivas(numero)
    print('Numero en binario: ',resultado.mostrar())
    input()