#Clases principales del sistema de citas médicas
#Gestión y búsqueda de pacientes registrados
class Paciente:
    def __init__(self, dni, nombres, apellidos, edad, telefono):
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono
    def mostrar_informacion(self):
        print("DNI:", self.dni)
        print("Nombres:", self.nombres)
        print("Apellidos:", self.apellidos)
        print("Edad:", self.edad)
        print("Teléfono:", self.telefono)
     
