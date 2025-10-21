from arbol import Arbol
from tipo_aceituna import TipoAceituna

class Olivo(Arbol):
    """Cultivo tipo Olivo."""

    def __init__(self, superficie: float, altura: float, tipo_aceituna: TipoAceituna):
        super().__init__("Olivo", superficie, altura)
        self.tipo_aceituna = tipo_aceituna
        self.produccion_anual = 0

    def absorber_agua(self, cantidad: float) -> None:
        if cantidad < 5:
            raise ValueError("El olivo necesita al menos 5 L de agua para mantenerse.")
        self.produccion_anual += cantidad * 0.2
