import unittest
import os
import shutil
from python_forestacion.servicios.negocio.fincas_service import FincasService
from python_forestacion.servicios.negocio.paquete import Paquete
from python_forestacion.Entidades.terrenos.plantacion import Plantacion
from python_forestacion.excepciones.persistencia_exception import PersistenciaException


class TestFincasService(unittest.TestCase):
    """Pruebas para el servicio de creación y registro de fincas."""

    def setUp(self):
        """Configuración antes de cada test."""
        self.service = FincasService()
        self.test_dir = "data_test"
        self.paquete = Paquete(self.test_dir)
        
        # Crear directorio de pruebas si no existe
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

    def tearDown(self):
        """Limpieza después de cada test."""
        # Eliminar directorio de pruebas completo
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_crear_finca(self):
        """Verificar que se puede crear una finca correctamente."""
        tierra = self.service.crear_finca(
            id_padron=1,
            superficie=50.0,
            domicilio="Ruta 7",
            nombre_plantacion="Finca Test"
        )
        
        self.assertEqual(tierra.id_padron, 1)
        self.assertEqual(tierra.superficie, 50.0)
        self.assertEqual(tierra.domicilio, "Ruta 7")
        self.assertEqual(tierra.nombre_plantacion, "Finca Test")
        self.assertIsNotNone(tierra.plantacion)
        self.assertIsInstance(tierra.plantacion, Plantacion)

    def test_persistencia_registro(self):
        """Verificar que el registro se puede persistir."""
        # Crear finca
        self.service.crear_finca(1, 50.0, "Ruta 7", "Finca Test")
        
        # Guardar registro
        registro = self.service.obtener_registro()
        self.paquete.guardar(registro, "registro_test")
        
        # Verificar que el archivo existe
        archivo_path = os.path.join(self.test_dir, "registro_test.dat")
        self.assertTrue(os.path.exists(archivo_path))
        
        # Verificar que el archivo no está vacío
        size = os.path.getsize(archivo_path)
        self.assertGreater(size, 0)
    
    def test_recuperar_registro(self):
        """Verificar que se puede recuperar un registro guardado."""
        # Crear y guardar finca
        self.service.crear_finca(1, 50.0, "Ruta 7", "Finca Test")
        registro = self.service.obtener_registro()
        self.paquete.guardar(registro, "registro_test")
        
        # Recuperar registro
        registro_recuperado = self.paquete.cargar("registro_test")
        
        # Verificar contenido
        self.assertIsNotNone(registro_recuperado)
        plantaciones = registro_recuperado.listar_todas()
        self.assertEqual(len(plantaciones), 1)
        self.assertEqual(plantaciones[0].nombre, "Finca Test")
    
    def test_multiples_fincas(self):
        """Verificar que se pueden crear múltiples fincas."""
        finca1 = self.service.crear_finca(1, 100.0, "Ruta 1", "Finca 1")
        finca2 = self.service.crear_finca(2, 200.0, "Ruta 2", "Finca 2")
        finca3 = self.service.crear_finca(3, 300.0, "Ruta 3", "Finca 3")
        
        tierras = self.service.listar_tierras()
        self.assertEqual(len(tierras), 3)
        
        plantaciones = self.service.listar_plantaciones()
        self.assertEqual(len(plantaciones), 3)
    
    def test_buscar_plantacion(self):
        """Verificar que se puede buscar una plantación por nombre."""
        self.service.crear_finca(1, 50.0, "Ruta 7", "Finca Test")
        
        plantacion = self.service.buscar_plantacion("Finca Test")
        self.assertIsNotNone(plantacion)
        self.assertEqual(plantacion.nombre, "Finca Test")
        
        # Buscar plantación inexistente
        plantacion_inexistente = self.service.buscar_plantacion("No Existe")
        self.assertIsNone(plantacion_inexistente)
    
    def test_eliminar_finca(self):
        """Verificar que se puede eliminar una finca."""
        self.service.crear_finca(1, 50.0, "Ruta 7", "Finca Test")
        
        # Verificar que existe
        plantaciones_antes = self.service.listar_plantaciones()
        self.assertEqual(len(plantaciones_antes), 1)
        
        # Eliminar
        resultado = self.service.eliminar_finca("Finca Test")
        self.assertTrue(resultado)
        
        # Verificar que ya no existe
        plantaciones_despues = self.service.listar_plantaciones()
        self.assertEqual(len(plantaciones_despues), 0)
    
    def test_error_archivo_inexistente(self):
        """Verificar que se lanza excepción al cargar archivo inexistente."""
        with self.assertRaises(PersistenciaException):
            self.paquete.cargar("archivo_inexistente")


if __name__ == "__main__":
    unittest.main()