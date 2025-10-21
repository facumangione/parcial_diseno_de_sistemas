import unittest
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.forestacion_exception import ForestacionException

class TestExcepciones(unittest.TestCase):
    """Verifica que las excepciones personalizadas funcionen correctamente."""

    def test_herencia_forestacion_exception(self):
        exc = AguaAgotadaException()
        self.assertTrue(isinstance(exc, ForestacionException))

    def test_mensaje_personalizado(self):
        exc = PersistenciaException("Error al guardar")
        self.assertIn("Error al guardar", str(exc))

    def test_instanciacion_superficie(self):
        exc = SuperficieInsuficienteException()
        self.assertTrue("Superficie insuficiente" in str(exc))


if __name__ == "__main__":
    unittest.main()
