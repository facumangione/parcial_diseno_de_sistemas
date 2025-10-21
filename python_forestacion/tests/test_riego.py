import unittest
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask
from constante import TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO


class TestSistemaRiego(unittest.TestCase):
    """Pruebas para el subsistema de riego y patrón Observer."""

    def setUp(self):
        """Configuración antes de cada test."""
        self.sensor_temp = TemperaturaReaderTask()
        self.sensor_hum = HumedadReaderTask()
        self.controlador = ControlRiegoTask()
        
        # Registrar observadores
        self.sensor_temp.agregar_observador(self.controlador)
        self.sensor_hum.agregar_observador(self.controlador)

    def test_creacion_sensores(self):
        """Verificar que los sensores se crean correctamente."""
        self.assertIsNotNone(self.sensor_temp)
        self.assertIsNotNone(self.sensor_hum)
        self.assertEqual(self.sensor_temp.tipo, "temperatura")
        self.assertEqual(self.sensor_hum.tipo, "humedad")

    def test_creacion_controlador(self):
        """Verificar que el controlador se crea correctamente."""
        self.assertIsNotNone(self.controlador)
        self.assertIsNone(self.controlador.temperatura)
        self.assertIsNone(self.controlador.humedad)
        self.assertFalse(self.controlador.riego_activado)

    def test_notificacion_sensores(self):
        """Los sensores deben actualizar el controlador al hacer lecturas."""
        # Hacer lecturas
        temp = self.sensor_temp.leer_temperatura()
        hum = self.sensor_hum.leer_humedad()
        
        # Verificar que el controlador recibió las notificaciones
        self.assertIsNotNone(self.controlador.temperatura)
        self.assertIsNotNone(self.controlador.humedad)
        self.assertEqual(self.controlador.temperatura, temp)
        self.assertEqual(self.controlador.humedad, hum)
        
        # Verificar que el estado se puede obtener
        estado = self.controlador.estado_riego()
        self.assertIn("Riego", estado)

    def test_rango_temperatura(self):
        """Verificar que las lecturas de temperatura están en rango válido."""
        for _ in range(10):
            temp = self.sensor_temp.leer_temperatura()
            self.assertGreaterEqual(temp, 5)  # Límite inferior según código
            self.assertLessEqual(temp, 40)    # Límite superior según código

    def test_rango_humedad(self):
        """Verificar que las lecturas de humedad están en rango válido."""
        for _ in range(10):
            hum = self.sensor_hum.leer_humedad()
            self.assertGreaterEqual(hum, 10)  # Límite inferior según código
            self.assertLessEqual(hum, 80)     # Límite superior según código

    def test_logica_activacion_riego(self):
        """Verificar que el riego se activa/desactiva según las condiciones."""
        # Condiciones que DEBERÍAN activar el riego:
        # Temperatura entre 8-15°C Y humedad < 50%
        
        # Caso 1: Condiciones ideales para riego
        self.sensor_temp.actualizar_valor(10)  # En rango [8, 15]
        self.sensor_hum.actualizar_valor(30)   # < 50%
        self.assertTrue(self.controlador.riego_activado)
        
        # Caso 2: Temperatura muy alta
        self.sensor_temp.actualizar_valor(25)  # Fuera de rango [8, 15]
        self.sensor_hum.actualizar_valor(30)   # < 50%
        self.assertFalse(self.controlador.riego_activado)
        
        # Caso 3: Humedad muy alta
        self.sensor_temp.actualizar_valor(10)  # En rango [8, 15]
        self.sensor_hum.actualizar_valor(80)   # >= 50%
        self.assertFalse(self.controlador.riego_activado)
        
        # Caso 4: Temperatura muy baja
        self.sensor_temp.actualizar_valor(5)   # Fuera de rango [8, 15]
        self.sensor_hum.actualizar_valor(30)   # < 50%
        self.assertFalse(self.controlador.riego_activado)

    def test_estado_riego_dinamico(self):
        """El estado del riego debe cambiar según lecturas."""
        # Primera lectura - activar riego
        self.sensor_temp.actualizar_valor(12)
        self.sensor_hum.actualizar_valor(20)
        estado1 = self.controlador.estado_riego()
        self.assertIn("ACTIVADO", estado1)
        
        # Segunda lectura - desactivar riego
        self.sensor_temp.actualizar_valor(40)
        self.sensor_hum.actualizar_valor(80)
        estado2 = self.controlador.estado_riego()
        self.assertIn("reposo", estado2)
        
        # Los estados deben ser diferentes
        self.assertNotEqual(estado1, estado2)

    def test_multiples_observadores(self):
        """Verificar que se pueden agregar múltiples observadores."""
        controlador2 = ControlRiegoTask()
        
        # Agregar segundo observador
        self.sensor_temp.agregar_observador(controlador2)
        self.sensor_hum.agregar_observador(controlador2)
        
        # Hacer lectura
        temp = self.sensor_temp.leer_temperatura()
        hum = self.sensor_hum.leer_humedad()
        
        # Ambos controladores deben recibir notificaciones
        self.assertEqual(self.controlador.temperatura, temp)
        self.assertEqual(controlador2.temperatura, temp)
        self.assertEqual(self.controlador.humedad, hum)
        self.assertEqual(controlador2.humedad, hum)

    def test_eliminar_observador(self):
        """Verificar que se puede eliminar un observador."""
        # Hacer lectura inicial
        self.sensor_temp.leer_temperatura()
        temp_inicial = self.controlador.temperatura
        self.assertIsNotNone(temp_inicial)
        
        # Eliminar observador
        self.sensor_temp.eliminar_observador(self.controlador)
        
        # Nueva lectura no debería actualizar el controlador
        self.sensor_temp.leer_temperatura()
        # El controlador mantiene el valor anterior
        self.assertEqual(self.controlador.temperatura, temp_inicial)

    def test_estado_sin_lecturas(self):
        """Verificar estado cuando no hay lecturas."""
        controlador_nuevo = ControlRiegoTask()
        estado = controlador_nuevo.estado_riego()
        
        # Debe contener "None" porque no hay lecturas
        self.assertIn("None", estado)

    def test_condiciones_limite_riego(self):
        """Probar condiciones límite de activación de riego."""
        # Límite inferior de temperatura (8°C)
        self.sensor_temp.actualizar_valor(TEMP_MIN_RIEGO)
        self.sensor_hum.actualizar_valor(30)
        self.assertTrue(self.controlador.riego_activado)
        
        # Límite superior de temperatura (15°C)
        self.sensor_temp.actualizar_valor(TEMP_MAX_RIEGO)
        self.sensor_hum.actualizar_valor(30)
        self.assertTrue(self.controlador.riego_activado)
        
        # Límite de humedad (50%)
        self.sensor_temp.actualizar_valor(10)
        self.sensor_hum.actualizar_valor(HUMEDAD_MAX_RIEGO - 1)
        self.assertTrue(self.controlador.riego_activado)
        
        # Justo fuera del límite de humedad
        self.sensor_temp.actualizar_valor(10)
        self.sensor_hum.actualizar_valor(HUMEDAD_MAX_RIEGO)
        self.assertFalse(self.controlador.riego_activado)


if __name__ == "__main__":
    unittest.main()