from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.Entidades.cultivos.olivo import Olivo

class OlivoService(ArbolService):
    """Servicio para manejar cultivos de tipo Olivo."""

    def __init__(self, cultivo: Olivo):
        super().__init__(cultivo)

    def validar_cultivo(self) -> bool:
        return self._cultivo.altura >= 0.5 and self._cultivo.produccion_anual >= 0

    def registrar(self) -> str:
        return f"Olivo ({self._cultivo.tipo_aceituna.value}) registrado correctamente."
