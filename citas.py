#Validación y gestión de citas médicas
class CitaMedica:
    def __init__(self, codigo, paciente, fecha, especialidad, medico):
        self.codigo = codigo
        self.paciente = paciente
        self.fecha = fecha
        self.especialidad = especialidad
        self.medico = medico
    def mostrar_informacion(self):
        print("Código:", self.codigo)
        print("Paciente:", self.paciente)
        print("Fecha:", self.fecha)
        print("Especialidad:", self.especialidad)
        print("Médico:", self.medico)
