from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import MENSAJE_SUPERFICIE

class SuperficieInsuficienteException(ForestacionException):
    """Excepción lanzada cuando un cultivo excede la superficie disponible."""

    def __init__(self):
        super().__init__(MENSAJE_SUPERFICIE)
