from python_forestacion.Entidades.terrenos.tierra import Tierra
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException

class TierraService:
    """Servicio para gestionar las tierras registradas."""

    def __init__(self):
        self._tierras: dict[int, Tierra] = {}

    def registrar_tierra(self, tierra: Tierra):
        if tierra.superficie <= 0:
            raise SuperficieInsuficienteException()
        self._tierras[tierra.id_padron] = tierra

    def listar_tierras(self) -> list[Tierra]:
        return list(self._tierras.values())
