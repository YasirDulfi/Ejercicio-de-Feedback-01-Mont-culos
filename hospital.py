import random
from heap import MaxHeap
from heap import MinHeap

class Paciente:
    def __init__(self, nombre, nivel_urgencia, horas_espera):
        self.nombre = nombre
        self.nivel_urgencia = nivel_urgencia
        self.horas_espera = horas_espera

class SalaEmergencias:
    def __init__(self):
        self.max_heap_urgencia = MaxHeap(20)
        self.min_heap_tiempo = MinHeap(20)
        self.pacientes_atendidos = []

    def agregar_paciente(self, paciente):
        self.max_heap_urgencia.insert(paciente)
        self.min_heap_tiempo.insert(paciente)

    def atender_pacientes(self, num_pacientes):
        for index in range(num_pacientes):
            print("Index: "+str(index))
            paciente_atendido = None
            # Priorizar pacientes con nivel de urgencia 10
            if not self.max_heap_urgencia.isEmpty() and self.max_heap_urgencia.peek().nivel_urgencia == 10:
                print("if 1: Se prioriza nivel 10")
                paciente_atendido = self.atender_paciente_por_urgencia(10)
            # Priorizar pacientes con un tiempo de espera mayor o igual a 5
            elif not self.min_heap_tiempo.isEmpty() and bool(self.min_heap_tiempo.peekByTime()):
                print("if 2: Se prioriza tiempo menor a 5")
                paciente_atendido = self.atender_paciente_por_tiempo()
                print("El paciente "+str(paciente_atendido.horas_espera))
            # Priorizar paciencietes por urgencia con tiempo menor a 5
            elif not self.max_heap_urgencia.isEmpty():
                print("if 3: se prioriza mayor urgencia")
                paciente_atendido = self.atender_paciente_por_urgencia(self.max_heap_urgencia.heap[0].nivel_urgencia)
                print("El paciente "+str(paciente_atendido.horas_espera))

            if paciente_atendido:
                self.pacientes_atendidos.append(paciente_atendido)

    def atender_paciente_por_urgencia(self, nivel_urgencia):
        paciente_urgencia = self.max_heap_urgencia.peek()

        if paciente_urgencia.nivel_urgencia == nivel_urgencia:
            self.max_heap_urgencia.removeMax()
            self.min_heap_tiempo.eliminarPaciente(paciente_urgencia)
            return paciente_urgencia

    def atender_paciente_por_tiempo(self):
        paciente_tiempo = self.min_heap_tiempo.peekByTime()
        self.min_heap_tiempo.eliminarPaciente(paciente_tiempo)
        self.max_heap_urgencia.eliminarPaciente(paciente_tiempo)

        return paciente_tiempo

    def ordenFinalAtencion(self):
        for index, personaAtendida in enumerate(self.pacientes_atendidos):
            print(f'Posición {index}: Persona -> {personaAtendida.nombre}| nivel de urgencia: {personaAtendida.nivel_urgencia} | tiempo de atención: {personaAtendida.horas_espera}')
# Creamos la sala de emergencia 
sala_emergencias = SalaEmergencias()

#Generamos los pacientes
for index in range(20):
    paciente = Paciente(f'Paciente{index}', random.randint(1, 10), random.randint(1, 10))
    sala_emergencias.agregar_paciente(paciente)


sala_emergencias.atender_pacientes(20)

sala_emergencias.ordenFinalAtencion()


