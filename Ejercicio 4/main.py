from pilaSecuencial import Pila

if __name__ == '__main__':
    objeto = Pila(8)
    band = False
    print('Ingrese 0 para finalizar')
    while not band:
        Input = input('Ingrese "Numero/Pila": ')
        if(Input != '0'):
            Input = Input.split('/')
            if(Input[1] == '1'):
                if(objeto.insertar1(Input[0]) == 0):
                    print('ERROR: pila llena')
            elif(Input[1] == '2'):
                if(objeto.insertar2(Input[0]) == 0):
                    print('ERROR: pila llena')
            else:
                print('ERROR: pila no existente')
        else:
            band = True
    print('Elementos de la pila 1: {}'.format(objeto.mostrar1()))
    print('Elementos de la pila 2: {}'.format(objeto.mostrar2()))