from colaSecuencial import Cola

from colaEncadenada import cola

from manejador import Manejador

def consultorio(manejador): #crea la cola del consultorio
    consultorio = cola()

def especialidad(manejador): #crea la cola de las especialidades
    especialidades = ['Ginecologia', 'Clinica medica', 'Oftamologia', 'Pediatria']
    for especialidad in especialidades:
        cola = Cola(10, especialidad)
        manejador.addCola(cola)
if __name__ == '__main__':
    manejador = Manejador()
    #consultorio(manejador) #Intentar con la cola escalonada
    especialidad(manejador)
    tiempo1 = 0
    tiempo2 = 0
    while tiempo1 < 10: #4 horas = 240 minutos
        if(tiempo2 == 1): #llegada del paciente a la cola del consultorio
            manejador.addPacienteCola(-1) 
            tiempo2 = 0
        #if(manejador.atencion())
        #incrementar tiempo de las colas
        tiempo2 += 1
        tiempo1 += 1
    #mostrar los promedios y cantidad de pacientes no atendidos