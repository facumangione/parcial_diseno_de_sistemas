from cultivo_service import CultivoService
from python_forestacion.Entidades.cultivos.lechuga import Lechuga

class LechugaService(CultivoService):
    """Servicio para manejar cultivos de tipo Lechuga."""

    def __init__(self, cultivo: Lechuga):
        super().__init__(cultivo)

    def validar_cultivo(self) -> bool:
        return self._cultivo.dias_crecimiento <= 90

    def registrar(self) -> str:
        return "Lechuga registrada correctamente."
