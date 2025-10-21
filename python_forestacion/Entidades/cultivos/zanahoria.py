from hortaliza import Hortaliza

class Zanahoria(Hortaliza):
    """Cultivo tipo Zanahoria."""

    def __init__(self, superficie: float, dias_crecimiento: int, profundidad: float):
        super().__init__("Zanahoria", superficie, dias_crecimiento)
        self.profundidad = profundidad

    def absorber_agua(self, cantidad: float) -> None:
        if cantidad < 0.5:
            raise ValueError("La zanahoria requiere al menos 0.5 L de agua.")
        self.regar()
