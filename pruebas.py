#Pruebas unitarias para las funciones de citas médicas
import unittest

from citas import CitaMedica
from funciones import (
    filtrar_por_especialidad,
    filtrar_por_medico,
    transformar_fechas,
    ordenar_por_fecha
)
class TestCitasMedicas(unittest.TestCase):

    def setUp(self):
        self.citas = [
            CitaMedica(
                "C001",
                "Juan Pérez",
                "2026-09-25",
                "Cardiología",
                "Dr. Pérez"
            ),
            CitaMedica(
                "C002",
                "María López",
                "2026-09-20",
                "Cardiología",
                "Dr. Gómez"
            ),
            CitaMedica(
                "C003",
                "Carlos Ruiz",
                "2026-09-28",
                "Pediatría",
                "Dr. Pérez"
            )
        ]
    def test_filtrar_cardiologia(self):
        resultado = filtrar_por_especialidad(
            self.citas,
            "Cardiología"
        )
        self.assertEqual(len(resultado), 2)

    def test_filtrar_medico(self):
        resultado = filtrar_por_medico(
            self.citas,
            "Dr. Pérez"
        )
        self.assertEqual(len(resultado), 2)

    def test_transformar_fechas(self):
        resultado = transformar_fechas(self.citas)

        self.assertEqual(
            resultado,
            [
                "2026-09-25",
                "2026-09-20",
                "2026-09-28"
            ]
        )
    def test_ordenar_por_fecha(self):
        resultado = ordenar_por_fecha(self.citas)

        self.assertEqual(
            resultado[0].fecha,
            "2026-09-20"
        )
if __name__ == "__main__":
    unittest.main()
