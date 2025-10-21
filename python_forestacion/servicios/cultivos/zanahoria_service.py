from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.Entidades.cultivos.zanahoria import Zanahoria

class ZanahoriaService(CultivoService):
    """Servicio para manejar cultivos de tipo Zanahoria."""

    def __init__(self, cultivo: Zanahoria):
        super().__init__(cultivo)

    def validar_cultivo(self) -> bool:
        return self._cultivo.profundidad >= 0.2

    def registrar(self) -> str:
        return "Zanahoria registrada correctamente."
