from forestacion_exception import ForestacionException
from mensajes_exception import MENSAJE_PERSISTENCIA

class PersistenciaException(ForestacionException):
    """Excepción lanzada cuando ocurre un error al persistir o cargar datos."""

    def __init__(self, detalle: str = ""):
        mensaje = MENSAJE_PERSISTENCIA
        if detalle:
            mensaje += f" Detalle: {detalle}"
        super().__init__(mensaje)
