#Funciones para gestionar las citas médicas

#Filtra las citas según la especialidad médica
def filtrar_por_especialidad(citas, especialidad):
    return list(filter(
        lambda cita: cita.especialidad.lower() == especialidad.lower(),
        citas
    ))

#Filtrar citas según el médico tratante
def filtrar_por_medico(citas, medico):
    return list(filter(
        lambda cita: cita.medico.lower() == medico.lower(),
        citas
    ))

#Obtener las fechas de las citas registradas
def transformar_fechas(citas):
    return list(map(
        lambda cita: cita.fecha,
        citas
    ))
def ordenar_por_fecha(citas):
    return sorted(
        citas,
        key=lambda cita: cita.fecha
    )
