import unittest
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

class TestSistemaRiego(unittest.TestCase):
    """Pruebas para el subsistema de riego y patrón Observer."""

    def setUp(self):
        self.sensor_temp = TemperaturaReaderTask()
        self.sensor_hum = HumedadReaderTask()
        self.controlador = ControlRiegoTask()
        self.sensor_temp.agregar_observador(self.controlador)
        self.sensor_hum.agregar_observador(self.controlador)

    def test_notificacion_sensores(self):
        """Los sensores deben actualizar el controlador."""
        temp = self.sensor_temp.leer_temperatura()
        hum = self.sensor_hum.leer_humedad()
        self.assertIsNotNone(self.controlador.temperatura)
        self.assertIsNotNone(self.controlador.humedad)
        self.assertIn("Riego", self.controlador.estado_riego())

    def test_estado_riego_dinamico(self):
        """El estado del riego debe cambiar según lecturas."""
        self.sensor_temp.actualizar_valor(25)
        self.sensor_hum.actualizar_valor(20)
        estado1 = self.controlador.estado_riego()
        self.sensor_temp.actualizar_valor(40)
        self.sensor_hum.actualizar_valor(80)
        estado2 = self.controlador.estado_riego()
        self.assertNotEqual(estado1, estado2)


if __name__ == "__main__":
    unittest.main()
