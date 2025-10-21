from abc import ABC, abstractmethod

class Cultivo(ABC):
    """Clase base para todos los cultivos."""

    def __init__(self, nombre: str, superficie: float):
        self.nombre = nombre
        self.superficie = superficie

    @abstractmethod
    def absorber_agua(self, cantidad: float) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.nombre} ({self.superficie} m²)"
