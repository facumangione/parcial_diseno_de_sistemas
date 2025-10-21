from abc import ABC, abstractmethod

class AbsorcionAguaStrategy(ABC):
    """Interfaz para estrategias de absorción de agua."""

    @abstractmethod
    def absorber(self, cantidad: float) -> float:
        pass
