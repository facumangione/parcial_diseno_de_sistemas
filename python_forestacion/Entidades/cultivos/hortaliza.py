from cultivo import Cultivo

class Hortaliza(Cultivo):
    """Clase base para hortalizas (Lechuga, Zanahoria)."""

    def __init__(self, nombre: str, superficie: float, dias_crecimiento: int):
        super().__init__(nombre, superficie)
        self.dias_crecimiento = dias_crecimiento
        self.regada = False

    def regar(self) -> None:
        self.regada = True
