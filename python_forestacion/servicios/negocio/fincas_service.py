from python_forestacion.Entidades.terrenos.tierra import Tierra
from python_forestacion.Entidades.terrenos.plantacion import Plantacion
from python_forestacion.Entidades.terrenos.registro_forestal import RegistroForestal

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService


class FincasService:
    """
    Servicio de alto nivel que orquesta la creación y registro de fincas completas.
    Integra los servicios de Tierra, Plantación y RegistroForestal.
    """

    def __init__(self):
        self._tierra_service = TierraService()
        self._plantacion_service = PlantacionService()
        self._registro_forestal = RegistroForestal()
        self._registro_service = RegistroForestalService(self._registro_forestal)

    def crear_finca(self, id_padron: int, superficie: float, domicilio: str, nombre_plantacion: str) -> Tierra:
        """
        Crea una finca con su Tierra, Plantación y la registra automáticamente.
        """
        # Crear la tierra y plantación
        tierra = Tierra(id_padron, superficie, domicilio, nombre_plantacion)
        plantacion = Plantacion(nombre_plantacion, superficie, agua_disponible=100)

        # Asociar y registrar
        tierra.set_plantacion(plantacion)
        self._tierra_service.registrar_tierra(tierra)
        self._plantacion_service.registrar_plantacion(plantacion)
        self._registro_service.agregar_plantacion(plantacion)

        return tierra

    def listar_tierras(self):
        """Devuelve todas las tierras registradas."""
        return self._tierra_service.listar_tierras()

    def listar_plantaciones(self):
        """Devuelve todas las plantaciones registradas."""
        return self._registro_service.listar_todas()

    def buscar_plantacion(self, nombre: str):
        """Busca una plantación por su nombre."""
        return self._registro_service.buscar_plantacion(nombre)

    def eliminar_finca(self, nombre_plantacion: str) -> bool:
        """Elimina una finca del registro."""
        return self._registro_service.eliminar_plantacion(nombre_plantacion)

    def obtener_registro(self) -> RegistroForestal:
        """Devuelve el registro forestal activo."""
        return self._registro_forestal
