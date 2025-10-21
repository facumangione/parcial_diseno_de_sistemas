from python_forestacion.Entidades.cultivos.hortaliza import Hortaliza

class Lechuga(Hortaliza):
    """Cultivo tipo Lechuga."""

    def __init__(self, superficie: float, dias_crecimiento: int):
        super().__init__("Lechuga", superficie, dias_crecimiento)

    def absorber_agua(self, cantidad: float) -> None:
        if cantidad < 1:
            raise ValueError("La lechuga necesita al menos 1 L de agua.")
        self.regar()
