from forestacion_exception import ForestacionException
from mensajes_exception import MENSAJE_AGUA

class AguaAgotadaException(ForestacionException):
    """Excepción lanzada cuando la plantación no tiene agua suficiente."""

    def __init__(self):
        super().__init__(MENSAJE_AGUA)
