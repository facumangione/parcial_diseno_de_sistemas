from python_forestacion.patrones.singleton import singleton
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService

@singleton
class CultivoServiceRegistry:
    """Registro centralizado (Singleton) de servicios de cultivo."""

    def __init__(self):
        self._servicios: dict[str, CultivoService] = {}

    def registrar_servicio(self, nombre: str, servicio: CultivoService):
        self._servicios[nombre] = servicio

    def obtener_servicio(self, nombre: str) -> CultivoService | None:
        return self._servicios.get(nombre)

    def listar_servicios(self) -> list[str]:
        return list(self._servicios.keys())
