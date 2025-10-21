import unittest
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MENSAJE_SUPERFICIE,
    MENSAJE_AGUA,
    MENSAJE_PERSISTENCIA
)


class TestExcepciones(unittest.TestCase):
    """Verifica que las excepciones personalizadas funcionen correctamente."""

    def test_herencia_forestacion_exception(self):
        """Todas las excepciones deben heredar de ForestacionException."""
        exc_agua = AguaAgotadaException()
        exc_superficie = SuperficieInsuficienteException()
        exc_persistencia = PersistenciaException()
        
        self.assertIsInstance(exc_agua, ForestacionException)
        self.assertIsInstance(exc_superficie, ForestacionException)
        self.assertIsInstance(exc_persistencia, ForestacionException)

    def test_mensaje_personalizado(self):
        """PersistenciaException debe incluir detalles personalizados."""
        exc = PersistenciaException("Error al guardar")
        mensaje = str(exc)
        self.assertIn("Error al guardar", mensaje)
        self.assertIn("PythonForestal", mensaje)

    def test_instanciacion_superficie(self):
        """SuperficieInsuficienteException debe tener mensaje apropiado."""
        exc = SuperficieInsuficienteException()
        mensaje = str(exc).lower()
        # Verificar que contenga palabras clave relacionadas
        self.assertTrue(
            "superficie" in mensaje and "insuficiente" in mensaje,
            f"El mensaje '{str(exc)}' no contiene las palabras esperadas"
        )
    
    def test_agua_agotada_mensaje(self):
        """AguaAgotadaException debe mencionar agua."""
        exc = AguaAgotadaException()
        mensaje = str(exc).lower()
        self.assertIn("agua", mensaje)
    
    def test_formato_mensaje_base(self):
        """Todos los mensajes deben tener el prefijo [PythonForestal]."""
        excepciones = [
            AguaAgotadaException(),
            SuperficieInsuficienteException(),
            PersistenciaException("test")
        ]
        
        for exc in excepciones:
            self.assertIn("[PythonForestal]", str(exc))
    
    def test_mensaje_constantes(self):
        """Verificar que las excepciones usen las constantes correctas."""
        exc_superficie = SuperficieInsuficienteException()
        exc_agua = AguaAgotadaException()
        exc_persistencia = PersistenciaException()
        
        self.assertIn(MENSAJE_SUPERFICIE, str(exc_superficie))
        self.assertIn(MENSAJE_AGUA, str(exc_agua))
        self.assertIn(MENSAJE_PERSISTENCIA, str(exc_persistencia))
    
    def test_persistencia_con_detalle(self):
        """PersistenciaException debe agregar detalle al mensaje base."""
        detalle = "Archivo no encontrado: test.dat"
        exc = PersistenciaException(detalle)
        mensaje = str(exc)
        
        self.assertIn(MENSAJE_PERSISTENCIA, mensaje)
        self.assertIn(detalle, mensaje)
    
    def test_excepciones_son_exception(self):
        """Todas las excepciones deben ser subclase de Exception."""
        excepciones = [
            AguaAgotadaException(),
            SuperficieInsuficienteException(),
            PersistenciaException(),
            ForestacionException("test")
        ]
        
        for exc in excepciones:
            self.assertIsInstance(exc, Exception)


if __name__ == "__main__":
    unittest.main()