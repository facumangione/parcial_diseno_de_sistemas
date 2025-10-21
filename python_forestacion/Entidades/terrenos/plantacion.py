from python_forestacion.Entidades.cultivos.cultivo import Cultivo

class Plantacion:
    """Conjunto de cultivos dentro de una tierra."""

    def __init__(self, nombre: str, superficie: float, agua_disponible: float):
        self.nombre = nombre
        self.superficie = superficie
        self.agua_disponible = agua_disponible
        self.cultivos: list[Cultivo] = []

    def agregar_cultivo(self, cultivo: Cultivo) -> None:
        if cultivo.superficie > self.superficie:
            raise ValueError("Superficie insuficiente para agregar el cultivo.")
        self.cultivos.append(cultivo)

    def regar_todos(self, cantidad: float) -> None:
        if cantidad > self.agua_disponible:
            raise ValueError("Agua insuficiente en la plantación.")
        for cultivo in self.cultivos:
            cultivo.absorber_agua(cantidad)
        self.agua_disponible -= cantidad
