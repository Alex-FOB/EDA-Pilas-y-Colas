class Manejador:
    __colas = None
    __
    def __init__(self):
        self.__colas = []
    def addCola(self, cola):
        self.__colas.append(cola)
    def buscar(self, especialidad):
        pos = -1
        i = 0
        band = False
        while not band and i < len(self.__colas):
            if(self.__colas[i].getNombre() == especialidad):
                pos = i
            i += 1
        return pos
    def addPacienteCola(self, paciente): #añade un paciente a la cola del consultorio
        pass
    def addPacienteEsp(self, paciente): #añade un paciente a la cola de una especialidad
        pos = self.buscar(paciente.getEspecialidad())
        if(pos != -1):
            self.__colas[pos].insertar(paciente)