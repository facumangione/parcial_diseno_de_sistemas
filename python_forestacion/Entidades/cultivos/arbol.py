from python_forestacion.Entidades.cultivos.cultivo import Cultivo

class Arbol(Cultivo):
    """Clase base para árboles (Pino, Olivo)."""

    def __init__(self, nombre: str, superficie: float, altura: float):
        super().__init__(nombre, superficie)
        self.altura = altura
        self.produccion_anual = 0

    def crecer(self, metros: float) -> None:
        self.altura += metros
