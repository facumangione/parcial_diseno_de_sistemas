from abc import ABC, abstractmethod
from python_forestacion.Entidades.cultivos.cultivo import Cultivo

class CultivoService(ABC):
    """Servicio base para manejar cultivos."""

    def __init__(self, cultivo: Cultivo):
        self._cultivo = cultivo

    @abstractmethod
    def validar_cultivo(self) -> bool:
        pass

    @abstractmethod
    def registrar(self) -> str:
        pass
