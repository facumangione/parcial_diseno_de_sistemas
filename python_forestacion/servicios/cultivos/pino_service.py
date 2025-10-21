from arbol_service import ArbolService
from python_forestacion.Entidades.cultivos.pino import Pino
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException

class PinoService(ArbolService):
    """Servicio para manejar cultivos de tipo Pino."""

    def __init__(self, cultivo: Pino):
        super().__init__(cultivo)

    def validar_cultivo(self) -> bool:
        return self._cultivo.altura >= 1.0 and self._cultivo.superficie >= 5

    def absorber_agua(self, cantidad: float):
        if cantidad < 10:
            raise AguaAgotadaException()
        self._cultivo.absorber_agua(cantidad)
