# Ejercicio de Feedback 01: Montículos - Sistema de Prioridades en una Sala de Emergencias

Contexto del ejercicio :

Te encuentras a cargo de la administración de una sala de emergencias en un hospital. Los pacientes que ingresan a esta sala tienen distintos niveles de urgencia, y es crucial que sean atendidos en función de estas prioridades.

Clases:

    Paciente:

        Atributos: nombre, nivel_urgencia, horas_espera

    SalaEmergencias:

        Atributos:
    max_heap_urgencia (montículo máximo para urgencia),
    min_heap_tiempo (montículo mínimo para tiempo de espera)
    pacientes_atendidos (lista de los pacientes atendidos).

        Métodos:
    agregar_paciente(paciente): Agrega un paciente a ambos montículos.
    atender_pacientes(): Desencola y atender el paciente
    atender_paciente_por_urgencia(nivel_urgencia): Atiende el paciente dependiendo del nivel de urgencia
    atender_paciente_por_tiempo():Atiende el paciente dependiendo del orden de llegada sigueindo las reglas definidas posteriormente
    ordenFinalAtencion(): Nos muestra el orden de entrada y el orden de salida de los pacientes junto al nivel de urgencia y el tiempo de espera

Reglas:

    -Si hay pacientes con un nivel de urgencia de 10, atenderlos inmediatamente.
    -Si no hay pacientes con urgencia máxima pero hay pacientes que han esperado de 5 o más horas, atenderlos.
    -En caso contrario, atender al paciente con la mayor urgencia.

Simulación:

    1.Diseñamos las clases Paciente y SalaEmergencias.
    2.Generamos una lista de pacientes aleatorios con niveles de urgencia y tiempos de espera aleatorios.
    3.Añadimos estos pacientes a la SalaEmergencias, asegurándonos de incorporarlos a ambos montículos.
    4.Atendemos los pacientes segun las reglas predefinidas anteriormente

## Autor

Yasir Doulfikar Jouhri
