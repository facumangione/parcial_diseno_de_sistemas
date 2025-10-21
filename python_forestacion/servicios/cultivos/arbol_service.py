from cultivo_service import CultivoService
from python_forestacion.Entidades.cultivos.arbol import Arbol

class ArbolService(CultivoService):
    """Servicio base para cultivos de tipo árbol."""

    def __init__(self, arbol: Arbol):
        super().__init__(arbol)

    def validar_cultivo(self) -> bool:
        return self._cultivo.altura > 0

    def registrar(self) -> str:
        return f"Árbol {self._cultivo.nombre} registrado con altura {self._cultivo.altura} m."
