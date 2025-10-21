import unittest
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.negocio.paquete import Paquete
import os

class TestFincasService(unittest.TestCase):
    """Pruebas para el servicio de creación y registro de fincas."""

    def setUp(self):
        self.service = FincasService()
        self.paquete = Paquete("data_test")
        if not os.path.exists("data_test"):
            os.mkdir("data_test")

    def tearDown(self):
        # Limpia archivos generados en pruebas
        if os.path.exists("data_test/registro_test.dat"):
            os.remove("data_test/registro_test.dat")

    def test_crear_finca(self):
        tierra = self.service.crear_finca(1, 50.0, "Ruta 7", "Finca Test")
        self.assertEqual(tierra.id_padron, 1)
        self.assertEqual(tierra.superficie, 50.0)
        self.assertIsNotNone(tierra.plantacion)

    def test_persistencia_registro(self):
        registro = self.service.obtener_registro()
        self.paquete.guardar(registro, "registro_test")
        self.assertTrue(os.path.exists("data_test/registro_test.dat"))


if __name__ == "__main__":
    unittest.main()
