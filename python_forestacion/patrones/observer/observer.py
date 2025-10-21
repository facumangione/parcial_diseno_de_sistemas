from abc import ABC, abstractmethod

class Observer(ABC):
    """Interfaz Observer genérica."""

    @abstractmethod
    def actualizar(self, observable, *args, **kwargs):
        pass
